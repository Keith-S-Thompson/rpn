#!/usr/bin/python3

import sys
import math
import re
import readline

stack = []
unary_op = {
    (int, "--"):     int.__neg__,
    (float, "--"):   float.__neg__,
    (int, "1/"):     lambda x: 1 / x,
    (float, "1/"):   lambda x: 1.0 / x,
    (int, "!"):      math.factorial,

    (int, "sqrt"):    math.sqrt,
    (float, "sqrt"):  math.sqrt,
    (int, "exp"):     math.exp,
    (float, "exp"):   math.exp,
    (int, "ln"):      math.log,
    (float, "ln"):    math.log,
    (int, "loge"):    math.log,
    (float, "loge"):  math.log,
    (int, "log"):     math.log10,
    (float, "log"):   math.log10,
    (int, "log10"):   math.log10,
    (float, "log10"): math.log10,
    (int, "log2"):    math.log2,
    (float, "log2"):  math.log2,
    (int, "lg"):      math.log2,
    (float, "lg"):    math.log2,

    (int, "sin"):    math.sin,
    (float, "sin"):  math.sin,
    (int, "cos"):    math.cos,
    (float, "cos"):  math.cos,
    (int, "tan"):    math.tan,
    (float, "tan"):  math.tan,

    (int, "asin"):   math.asin,
    (float, "asin"): math.asin,
    (int, "acos"):   math.acos,
    (float, "acos"): math.acos,
    (int, "atan"):   math.atan,
    (float, "atan"): math.atan,
}
binary_op = {
    (int, int, "+"):  int.__add__,
    (int, int, "-"):  int.__sub__,
    (int, int, "*"):  int.__mul__,
    (int, int, "/"):  int.__truediv__,
    (int, int, "//"): int.__floordiv__,
    (int, int, "**"): int.__pow__,
    (int, int, "atan2"):  math.atan2,

    (float, float, "+"):  float.__add__,
    (float, float, "-"):  float.__sub__,
    (float, float, "*"):  float.__mul__,
    (float, float, "/"):  float.__truediv__,
    (float, float, "//"): float.__floordiv__,
    (float, float, "**"): float.__pow__,
    (float, float, "atan2"):  math.atan2,

    (int, float, "+"):  float.__add__,
    (int, float, "-"):  float.__sub__,
    (int, float, "*"):  float.__mul__,
    (int, float, "/"):  lambda x, y: x / y,
    (int, float, "//"): float.__floordiv__,
    (int, float, "**"): float.__pow__,
    (int, float, "atan2"):  math.atan2,

    (float, int, "+"):  float.__add__,
    (float, int, "-"):  float.__sub__,
    (float, int, "*"):  float.__mul__,
    (int, float, "/"):  float.__truediv__,
    (float, int, "//"): float.__floordiv__,
    (float, int, "**"): lambda x, y: x ** y,
    (float, int, "atan2"):  math.atan2,

    (str, str, "+"): str.__add__,
}


def type_abbrev(t):
    d = { int: "i", float: "f", str: "s" }
    pat = re.compile("^<class '.*'>$")
    if t in d:
        return d[t]
    elif pat.match(str(t)):
        return str(t).removeprefix("<class '").removesuffix("'>")
    else:
        return str(t)


def process_word(word):
    global stack
    global unary_op
    global binary_op

    if len(stack) >= 1 and (type(stack[0]), word) in unary_op:
        # print(">>> unary_op")
        stack[0] = unary_op[type(stack[0]), word](stack[0])

    elif len(stack) >= 2 and (type(stack[0]), type(stack[1]), word) in binary_op:
        # print(">>> binary_op")
        stack[1] = binary_op[type(stack[0]), type(stack[1]), word](stack[1], stack[0])
        del stack[0]

    elif word == "dup":
        if len(stack) == 0:
            print(f"{word} error: requires 1 argument")
        else:
            stack.insert(0, stack[0])

    elif word == "drop":
        if len(stack) == 0:
            print(f"{word} error: requires 1 argument")
        else:
            del stack[0]

    elif word == "swap":
        if len(stack) < 2:
            print(f"{word} error: requires 2 arguments")
        else:
            stack[0], stack[1] = stack[1], stack[0]

    elif word == "depth":
        stack.insert(0, len(stack))

    elif word == "clear":
        stack = []

    elif word == "pi":
        stack.insert(0, 4.0 * math.atan2(1.0, 1.0))

    elif word == "e":
        stack.insert(0, math.e)

    elif word == "pi":
        stack.insert(0, math.pi)

    elif word == "tau":
        stack.insert(0, math.tau)

    elif word == "inf":
        stack.insert(0, math.inf)

    elif word == "nan":
        stack.insert(0, math.nan)

    elif word == "int":
        if len(stack) < 1:
            print(f"{word} error: requires 1 argument")
        try:
            stack[0] = int(stack[0])
        except:
            print(f"{word} error, bad operand")

    elif word == "float":
        if len(stack) < 1:
            print(f"{word} error: requires 1 argument")
        try:
            stack[0] = float(stack[0])
        except:
            print(f"{word} error, bad operand")

    elif word == "str":
        if len(stack) < 1:
            print(f"{word} error: requires 1 argument")
        try:
            stack[0] = str(stack[0])
        except:
            print(f"{word} error, bad operand")

    else:
        try:
            stack.insert(0, int(word, base=0))
        except:
            try:
                stack.insert(0, float(word))
            except:
                stack.insert(0, word)


def process_line(line):
    if line.startswith(":"):
        line = line.removeprefix(":").removesuffix("\n")
        try:
            stack.insert(0, eval(line))
        except:
            print(": error, eval failed")
    else:
        for word in line.split():
            process_word(word)

def show_stack():
    global stack
    for i in reversed(range(len(stack))):
        print(f"{i:3}: {type_abbrev(type(stack[i]))}: {stack[i]}")


if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        process_word(arg)
    show_stack()
else:
    while True:
        try:
            line = input("> ")
        except EOFError:
            print("")
            break
        process_line(line)
        show_stack()
