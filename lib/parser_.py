import re
from pprint import pprint

from .classes.line import Line
from .classes.variable import Variable
from .classes.expression import Expression
from .classes.head import Head
from .classes.method import Method
from .classes.headfunc import HeadFunc
from .classes.value import Value

from .func_list import HEAD_FUNC_LIST, CHAIN_FUNC_LIST


def parse(source: str) -> list[Line]:
    lines = re.sub(r"[\r\n\t]", "", re.sub(r"(?m)\/\/.*?$", "", source)).split(";")

    ret: list[Line] = []
    for i in lines:
        if re.fullmatch(r"[ \r\n\t]*", i):
            continue
        ret.append(parse_line(i))
        # print(ret[-1])
    return ret


def parse_line(line: str) -> Line:
    assert line.count("=") == 1
    lhs, rhs = map(str.strip, line.split("="))
    assert re.fullmatch(r"[a-zA-Z_]+", lhs)
    return Line(parse_variable(lhs), parse_expression(rhs))


def parse_variable(variable: str) -> Variable:
    return Variable(variable)


def parse_headfunc(headfunc: str) -> HeadFunc:
    if "<" not in headfunc:
        return HeadFunc(headfunc, [])

    name = headfunc[: headfunc.find("<")].strip()
    args_str = headfunc[headfunc.find("<") + 1 : -1]

    args = []
    idx = 0
    start_idx = 0
    nest_cnt = 0
    in_str = ""
    while idx < len(args_str):
        if in_str != "":
            if in_str == args_str[idx]:
                in_str = ""
            idx += 1
            continue
        if args_str[idx] in "'\"":
            in_str = args_str[idx]
        if args_str[idx] == "<" or args_str[idx] == "(":
            nest_cnt += 1
        if args_str[idx] == ">" or args_str[idx] == ")":
            nest_cnt -= 1
        if nest_cnt == 0 and args_str[idx] == ",":
            args.append(parse_expression(args_str[start_idx:idx].strip()))
            start_idx = idx + 1
        idx += 1
    last = args_str[start_idx:].strip()
    if last != "":
        args.append(parse_expression(last))
    return HeadFunc(name, args)


def parse_method(method: str) -> Method:
    name = method[: method.find("(")].strip()
    args_str = method[method.find("(") + 1 : -1]

    args = []
    idx = 0
    start_idx = 0
    nest_cnt = 0
    in_str = ""
    while idx < len(args_str):
        if in_str != "":
            if in_str == args_str[idx]:
                in_str = ""
            idx += 1
            continue
        if args_str[idx] in "'\"":
            in_str = args_str[idx]
        if args_str[idx] == "<" or args_str[idx] == "(":
            nest_cnt += 1
        if args_str[idx] == ">" or args_str[idx] == ")":
            nest_cnt -= 1
        if nest_cnt == 0 and args_str[idx] == ",":
            args.append(parse_expression(args_str[start_idx:idx].strip()))
            start_idx = idx + 1
        idx += 1
    last = args_str[start_idx:].strip()
    if last != "":
        args.append(parse_expression(last))
    return Method(name, args)


def parse_value(value: str) -> Value:
    if (value[0] == '"' and value[-1] == '"') or (value[0] == "'" and value[-1] == "'"):
        return Value(value[1:-1])
    elif re.fullmatch(r"-??[0-9]+", value):
        return Value(int(value))
    else:
        return Value(float(value))


def parse_head(head: str) -> Head:
    if re.fullmatch(r"[a-zA-Z_]*[ \t\n\r]*(<.*>)??", head):
        name = head
        if "<" in head and head[0] not in "'\"" and head[-1] not in "'\"":
            name = head[: head.find("<")].strip()
        if name in HEAD_FUNC_LIST:
            return Head(parse_headfunc(head))
        return Head(parse_variable(head))
    else:
        return Head(parse_value(head))


def parse_expression(expression: str) -> Expression:
    nest_cnt = 0
    in_str = ""

    idx = 0
    while idx < len(expression):
        if in_str != "":
            if in_str == expression[idx]:
                in_str = ""
            idx += 1
            continue
        if expression[idx] in "'\"":
            in_str = expression[idx]
        if expression[idx] == "<":
            nest_cnt += 1
        if expression[idx] == ">":
            nest_cnt -= 1
        if nest_cnt == 0 and expression[idx] == "~":
            break
        idx += 1
    head: Head = parse_head(expression[:idx].strip())

    chains: list[Method] = []

    start_idx = idx + 1
    idx += 1

    nest_cnt = 0
    in_str = ""
    while idx < len(expression):
        if in_str != "":
            if in_str == expression[idx]:
                in_str = ""
            idx += 1
            continue
        if expression[idx] in "'\"":
            in_str = expression[idx]
        if expression[idx] == "<" or expression[idx] == "(":
            nest_cnt += 1
        if expression[idx] == ">" or expression[idx] == ")":
            nest_cnt -= 1
        if nest_cnt == 0 and expression[idx] == "~":
            chains.append(parse_method(expression[start_idx:idx].strip()))
            start_idx = idx + 1
        idx += 1
    if expression[start_idx:].strip()!="":
        chains.append(parse_method(expression[start_idx:].strip()))
    return Expression(head, chains)
