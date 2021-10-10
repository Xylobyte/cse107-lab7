"""
A program that calculates expressions in reverse polish notation

file: rpn_calculator.py

author: Donovan Griego

Date: 10-10-2021

assignment: Lab 7
"""

import operator

# Available operators and their functions
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul,
       "/": operator.truediv, "^": operator.pow, "=": operator.eq}


def main():
    expression = input("Enter an expression separated by spaces >>> ")
    expression = expression.split(" ")
    stack = []  # Acts as a stack
    for i in expression:
        try:
            num = int(i)
            stack.append(num)   # Adding a value to the stack
        except ValueError:
            try:
                val1 = stack.pop()
                val2 = stack.pop()
                # Using the values in the function from ops
                stack.append(ops[i](val2, val1))
            except IndexError:
                print("Error; not enough operands for '{}'".format(i))
                exit(1)
            except KeyError:
                print("Error; invalid operator '{}'".format(i))
                exit(1)
    if len(stack) == 1:
        print(stack[0])
    else:
        print("Error; not enough operators")
        exit(1)


if __name__ == "__main__":
    main()
