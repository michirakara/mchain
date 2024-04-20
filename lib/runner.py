from collections import deque
from copy import deepcopy

from .classes.line import Line
from .classes.variable import Variable
from .classes.expression import Expression
from .classes.head import Head
from .classes.method import Method
from .classes.headfunc import HeadFunc
from .classes.value import Value
from .classes.function import Function

from .func_list import HEAD_FUNC_LIST, CHAIN_FUNC_LIST

vars: dict[str, Value] = dict()


def run(code: list[Line]) -> None:
    for line in code:
        vars[line.lhs.name] = run_expression(line.rhs)


def run_expression(expression: Expression) -> Value:
    val: Value
    if type(expression.head.val) == HeadFunc:
        val = run_headfunc(expression.head.val)
    elif type(expression.head.val) == Variable:
        val = vars[expression.head.val.name]
    else:
        val = expression.head.val

    for method in expression.chain:
        val = run_method(val, method)
    return val


def run_headfunc(headfunc: HeadFunc) -> Value:
    match headfunc.name:
        case "nextIn":
            args: list[Value] = [run_expression(i) for i in headfunc.args]
            return nextIn_(*args)
        case "newList":
            args: list[Value] = [run_expression(i) for i in headfunc.args]
            return newList_(*args)
        case "FUNC":
            func_variables = [i.head.val for i in headfunc.args[:-1]]
            return FUNC_(*func_variables, expression=headfunc.args[-1])


input_storage: deque[str] = deque()


def nextIn_() -> Value:
    while len(input_storage) == 0:
        for i in input().split():
            input_storage.append(i)
    return Value(input_storage.popleft())


def newList_(size: Value, value: Value) -> Value:
    return Value([deepcopy(value) for i in range(size.val)])


def FUNC_(*args: Variable, expression: Expression) -> Value:
    return Function(*args, expression=expression)


def run_func(*args: Value, func: Function) -> Value:
    for val, name in zip(args, func.vars):
        vars[name.name] = val
    return run_expression(func.expression)


def run_method(val: Value, method: Method) -> Value:
    args: list[Value] = [run_expression(i) for i in method.args]
    match method.name:
        case "add":
            return add_(val, *args)
        case "sub":
            return sub_(val, *args)
        case "mult":
            return mult_(val, *args)
        case "div":
            return div_(val, *args)
        case "pow":
            return pow_(val, *args)
        case "print":
            return print_(val, *args)
        case "println":
            return println_(val, *args)
        case "parseInt":
            return parseInt_(val, *args)
        case "parseFloat":
            return parseFloat_(val, *args)
        case "map":
            return map_(val, *args)
        case "at":
            return at_(val, *args)
        case "reduce":
            return reduce_(val, *args)
        case "eq":
            return eq_(val, *args)
        case "gt":
            return gt_(val, *args)
        case "lt":
            return lt_(val, *args)
        case "geq":
            return geq_(val, *args)
        case "leq":
            return leq_(val, *args)
        case "flip":
            return flip_(val, *args)
        case "iota":
            return iota_(val, *args)
        case "ifElse":
            return ifElse_(val, *args)
        case "set":
            return set_(val, *args)
        case "subSeq":
            return subSeq_(val, *args)
        case "and":
            return and_(val, *args)
        case "or":
            return or_(val, *args)
        case "xor":
            return xor_(val, *args)


def add_(lhs: Value, to_add: Value) -> Value:
    return Value(lhs.val + to_add.val)


def sub_(lhs: Value, to_sub: Value) -> Value:
    return Value(lhs.val - to_sub.val)


def mult_(lhs: Value, to_mult: Value) -> Value:
    return Value(lhs.val * to_mult.val)


def div_(lhs: Value, to_div: Value) -> Value:
    return Value(lhs.val / to_div.val)


def pow_(lhs: Value, to_pow: Value) -> Value:
    return Value(lhs.val**to_pow.val)


def print_(lhs: Value) -> Value:
    print(lhs.val, end="")
    return lhs


def println_(lhs: Value) -> Value:
    print(lhs.val)
    return lhs


def parseInt_(lhs: Value) -> Value:
    return Value(int(lhs.val))


def parseFloat_(lhs: Value) -> Value:
    return Value(float(lhs.val))


def map_(lhs: Value, func: Value) -> Value:
    ret = deepcopy(lhs).val
    for i in range(len(lhs.val)):
        ret[i] = run_func(lhs.val[i], func=func)
    return Value(ret)


def at_(lhs: Value, idx: Value) -> Value:
    return lhs.val[idx.val]


def reduce_(lhs: Value, start_val: Value, func: Value) -> Value:
    val = deepcopy(start_val)
    for i in lhs.val:
        val = run_func(val, i, func=func)
    return val


def eq_(lhs: Value, rhs: Value) -> Value:
    return Value(lhs.val == rhs.val)


def gt_(lhs: Value, rhs: Value) -> Value:
    return Value(lhs.val > rhs.val)


def lt_(lhs: Value, rhs: Value) -> Value:
    return Value(lhs.val < rhs.val)


def geq_(lhs: Value, rhs: Value) -> Value:
    return Value(lhs.val >= rhs.val)


def leq_(lhs: Value, rhs: Value) -> Value:
    return Value(lhs.val <= rhs.val)


def flip_(lhs: Value) -> Value:
    return Value(not lhs.val)


def iota_(lhs: Value, begin: Value, step: Value) -> Value:
    now = begin.val
    to_ret = deepcopy(lhs).val
    for i in range(len(lhs.val)):
        to_ret[i] = Value(now)
        now += step.val
    return Value(to_ret)


def ifElse_(lhs: Value, condition: Value, iftrue: Value, iffalse: Value) -> Value:
    if condition.val:
        return run_func(lhs, func=iftrue)
    return run_func(lhs, func=iffalse)


def set_(lhs: Value, idx: Value, value: Value) -> Value:
    ret = deepcopy(lhs).val
    ret[idx.val] = value
    return Value(ret)


def subSeq_(lhs: Value, start: Value, end: Value) -> Value:
    return Value(deepcopy(lhs).val[start.val : end.val])


def and_(lhs: Value, rhs: Value) -> Value:
    return Value(lhs.val & rhs.val)


def or_(lhs: Value, rhs: Value) -> Value:
    return Value(lhs.val | rhs.val)


def xor_(lhs: Value, rhs: Value) -> Value:
    return Value(lhs.val ^ rhs.val)
