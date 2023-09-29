#!/usr/bin/python3

import sys
import math

def type_abbrev(t):
    d = { int: 'i', float: 'f', str: 's' }
    if t in d:
        return d[t]
    else:
        return str(t)


stack = []

for line in sys.stdin:
    if line.startswith(":"):
        line = line.removeprefix(":")
        line = line.removesuffix("\n")
        try:
            stack.insert(0, eval(line))
        except:
            print(": error, eval failed")
    else:
        for word in line.split():
            if word == "drop":
                if len(stack) == 0:
                    print("drop error: too few arguments")
                else:
                    del stack[0]

            elif word == "swap":
                if len(stack) < 2:
                    print("swap error: too few arguments")
                else:
                    stack[0], stack[1] = stack[1], stack[0]

            elif word == "depth":
                stack.insert(0, len(stack))

            elif word == "clear":
                stack = []

            elif word == "+":
                if len(stack) < 2:
                    print("+ error: too few arguments")
                else:
                    try:
                        stack[1] += stack[0]
                        del stack[0]
                    except:
                        print("+ error: bad arguments")

            elif word == "-":
                if len(stack) < 2:
                    print("- error: too few arguments")
                else:
                    try:
                        stack[1] -= stack[0]
                        del stack[0]
                    except:
                        print("- error: bad arguments")

            elif word == "*":
                if len(stack) < 2:
                    print("- error: too few arguments")
                else:
                    try:
                        stack[1] *= stack[0]
                        del stack[0]
                    except:
                        print("* error: bad arguments")

            elif word == "/":
                if len(stack) < 2:
                    print("- error: too few arguments")
                else:
                    try:
                        stack[1] /= stack[0]
                        del stack[0]
                    except:
                        print("/ error: bad arguments")

            elif word == "//":
                if len(stack) < 2:
                    print("// error: too few arguments")
                else:
                    try:
                        stack[1] //= stack[0]
                        del stack[0]
                    except:
                        print("// error: bad arguments")

            elif word == "**":
                if len(stack) < 2:
                    print("** error: too few arguments")
                else:
                    try:
                        stack[1] **= stack[0]
                        del stack[0]
                    except:
                        print("** error: bad arguments")

            else:
                try:
                    stack.insert(0, int(word, base=0))
                except:
                    try:
                        stack.insert(0, float(word))
                    except:
                        stack.insert(0, word)

    for i in reversed(range(len(stack))):
        print(f"{i:3}: {type_abbrev(type(stack[i]))}: {stack[i]}")
