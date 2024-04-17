from collections import deque

CHAIN_FUNC_LIST = [
    "add",
    "sub",
    "mult",
    "div",
    "pow",
    "print",
    "println",
    "parseInt",
    "parseFloat",
    "map",
    "at",
    "reduce",
    "eq",
    "gt",
    "lt",
    "geq",
    "leq",
    "flip",
    "iota",
    "ifElse",
]

BEGIN_FUNC_LIST = ["nextIn", "newList", "FUNC"]

input_storage = deque()


def nextIn_():
    while len(input_storage) == 0:
        for i in input().split():
            input_storage.append(i)
    return input_storage.popleft()


def newList_(size, value):
    return [value for _ in range(size)]


def FUNC_(*names, func):
    return Func(*names, func=func)


def parse_line(line):
    lhs, rhs = line.split("=")
    s = f"global {lhs}; {lhs} = {parse_expression(rhs).__repr__()}"
    # print(s)
    exec(s)


class Func:
    def __init__(self, *names, func):
        self.names = names
        self.func = func

    def __str__(self):
        return f"Func({self.names.__repr__()[1:-1].strip(',')},func={self.func.__repr__()})"

    def __repr__(self):
        return f"Func({self.names.__repr__()[1:-1].strip(',')},func={self.func.__repr__()})"


def parse_start(expression):
    # print("parse-start\t", expression)
    expression = expression.strip()
    is_func = False
    if expression[:5] == "FUNC<":
        is_func = True

    start_idx = expression.find("<")
    if start_idx == -1:
        start_idx = len(expression)
    if expression[:start_idx] in BEGIN_FUNC_LIST:
        args = []
        if start_idx != len(expression):
            args_str = expression[start_idx + 1 : len(expression) - 1]
            now = ""
            idx = 0
            nest_cnt = 0
            while idx < len(args_str):
                if args_str[idx] in "<(":
                    nest_cnt += 1
                if args_str[idx] in ">)":
                    nest_cnt -= 1
                if args_str[idx] == "," and nest_cnt == 0:
                    if now != "":
                        if not is_func:
                            args.append(parse_expression(now))
                        else:
                            args.append(now)
                    now = ""
                elif args_str[idx] != " ":
                    now += args_str[idx]
                idx += 1
            if now != "":
                # print(now)
                if not is_func:
                    args.append(parse_expression(now))
                else:
                    args.append(now)
        if is_func:
            # print(
            #    f"{expression[:start_idx]}_({args[:-1].__str__()[1:-1]},func={args[-1].__repr__()})"
            # )
            return eval(
                f"{expression[:start_idx]}_({args[:-1].__str__()[1:-1]},func={args[-1].__repr__()})"
            )
        else:
            # print(f"{expression[:start_idx]}_({args.__str__()[1:-1]})")
            return eval(f"{expression[:start_idx]}_({args.__str__()[1:-1]})")
    return eval(expression)


def parse_expression(expression):
    # print("parse-expression:\t", expression)
    expression = expression.strip()
    funcs = []
    now = ["", [""]]
    start_idx = len(expression)
    idx = 0
    nest_cnt = 0
    while idx < len(expression):
        if expression[idx] in "<(":
            nest_cnt += 1
        if expression[idx] in ">)":
            nest_cnt -= 1
        if expression[idx] == "~" and nest_cnt == 0:
            start_idx = expression.index("~")
            break
        idx += 1

    val = parse_start(expression[:start_idx])

    idx = start_idx + 1
    # print(expression[idx:])
    while idx < len(expression):
        if expression[idx] == "(":
            now[0] = now[0].strip()
            idx += 1
            nest_cnt = 0
            while expression[idx] != ")" or nest_cnt != 0:
                if expression[idx] in "<(":
                    nest_cnt += 1
                if expression[idx] in ">)":
                    nest_cnt -= 1
                if expression[idx] == "," and nest_cnt == 0:
                    now[1][-1] = parse_expression(now[1][-1])
                    now[1].append("")
                elif expression[idx] != " ":
                    now[1][-1] += expression[idx]
                idx += 1
            while now[1] and now[1][-1] == "":
                now[1].pop()
            if now[1] and type(now[1][-1]) == str:
                now[1][-1] = parse_expression(now[1][-1])
            funcs.append(now)
            now = ["", [""]]
            while idx < len(expression) and expression[idx] != "~":
                idx += 1
        elif expression[idx] != " ":
            now[0] += expression[idx]
        idx += 1

    # print(val, funcs)

    for name, args in funcs:
        # if name in CHAIN_FUNC_LIST:
        # print(name, val, args)
        # print(f"{name}_({val.__repr__()},{args.__str__()[1:-1]})")
        val = eval(f"{name}_({val.__repr__()},{args.__str__()[1:-1]})")
        # print("new:\t", val)

    return val


def call_func(*args, func):
    # print(args, func)
    for i in range(len(args)):
        exec(f"global {func.names[i]};{func.names[i]}={args[i]}")
    return parse_expression(func.func)


def add_(lhs, to_add):
    return lhs + to_add


def sub_(lhs, to_sub):
    return lhs - to_sub


def mult_(lhs, to_mult):
    return lhs * to_mult


def div_(lhs, to_div):
    return lhs / to_div


def pow_(lhs, to_pow):
    return lhs**to_pow


def print_(lhs):
    print(lhs, end="")
    return lhs


def println_(lhs):
    print(lhs)
    return lhs


def parseInt_(lhs):
    return int(lhs)


def parseFloat_(lhs):
    return float(lhs)


def map_(lhs, func):
    ret = lhs[:]
    for i in range(len(lhs)):
        ret[i] = call_func(lhs[i], func=func)
    return ret


def at_(lhs, idx):
    return lhs[idx]


def reduce_(lhs, start_val, func):
    val = start_val
    for i in lhs:
        val = call_func(val, i, func=func)
    return val


def eq_(lhs, rhs):
    return lhs == rhs


def gt_(lhs, rhs):
    return lhs > rhs


def lt_(lhs, rhs):
    return lhs < rhs


def geq_(lhs, rhs):
    return lhs >= rhs


def leq_(lhs, rhs):
    return lhs <= rhs


def flip_(lhs):
    return not lhs


def iota_(lhs, begin, step):
    now = begin
    to_ret = lhs[:]
    for i in range(len(lhs)):
        to_ret[i] = now
        now += step
    return to_ret


def ifElse_(lhs, condition, iftrue, iffalse):
    if condition:
        return call_func(lhs, func=iftrue)
    return call_func(lhs, func=iffalse)


def set_(lhs, idx, value):
    ret = lhs[:]
    ret[idx] = value
    return ret
