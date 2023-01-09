import re
from decimal import Decimal


def get_first_num(sub_or_full_equation, index):
    num = ""
    start = 0

    for i in range(index - 1, -1, -1):
        if sub_or_full_equation[i] != " " and sub_or_full_equation[i] != "(":
            num += sub_or_full_equation[i]
            if i == 0:
                start = i
        else:
            start = i + 1
            break

    return Decimal(num[::-1]), start


def get_second_num(sub_or_full_equation, index):
    num = ""
    end = 0

    for i in range(index + 3, len(sub_or_full_equation)):
        if sub_or_full_equation[i] != " " and sub_or_full_equation[i] != ")":
            num += sub_or_full_equation[i]
            if i == len(sub_or_full_equation) - 1:
                end = i + 1
        else:
            end = i
            break

    return Decimal(num), end


def addition(sub_or_full_equation):
    while " + " in sub_or_full_equation:
        plus_location = sub_or_full_equation.index(" + ")
        first_num, start = get_first_num(sub_or_full_equation, plus_location)
        second_num, end = get_second_num(sub_or_full_equation, plus_location)
        result = str(first_num + second_num)

        sub_or_full_equation = sub_or_full_equation[:start] + result \
                               + sub_or_full_equation[end:]

    return sub_or_full_equation


def subtraction(sub_or_full_equation):
    while " - " in sub_or_full_equation:
        minus_location = sub_or_full_equation.index(" - ")
        first_num, start = get_first_num(sub_or_full_equation, minus_location)
        second_num, end = get_second_num(sub_or_full_equation, minus_location)
        result = str(first_num - second_num)

        sub_or_full_equation = sub_or_full_equation[:start] + result \
                               + sub_or_full_equation[end:]

    return sub_or_full_equation


def multiplication(sub_or_full_equation):
    while " * " in sub_or_full_equation:
        multiplication_location = sub_or_full_equation.index(" * ")
        first_num, start = get_first_num(sub_or_full_equation, multiplication_location)
        second_num, end = get_second_num(sub_or_full_equation, multiplication_location)
        result = str(first_num * second_num)

        sub_or_full_equation = sub_or_full_equation[:start] + result \
                               + sub_or_full_equation[end:]

    return sub_or_full_equation


def division(sub_or_full_equation):
    while " / " in sub_or_full_equation:
        division_location = sub_or_full_equation.index(" / ")
        first_num, start = get_first_num(sub_or_full_equation, division_location)
        second_num, end = get_second_num(sub_or_full_equation, division_location)
        result = str(first_num / second_num)

        sub_or_full_equation = sub_or_full_equation[:start] + result \
                               + sub_or_full_equation[end:]

    return sub_or_full_equation


def bracket_solving(the_equation):
    while "(" in the_equation or ")" in the_equation:

        if "(" in the_equation and ")" in the_equation:
            bracket_expression = re.search(r"\(([^(]+?)\)", the_equation)
            bracket_expression_start = bracket_expression.start()
            bracket_expression_end = bracket_expression.end()
            bracket_expression = bracket_expression.group(1)

            bracket_expression = multiplication(bracket_expression)

            bracket_expression = division(bracket_expression)

            bracket_expression = addition(bracket_expression)

            bracket_expression = subtraction(bracket_expression)

            the_equation = the_equation[:bracket_expression_start] + bracket_expression \
                           + the_equation[bracket_expression_end:]

        elif "(" in the_equation or ")" in the_equation:
            print("Error, invalid syntax.")
            exit()

    return the_equation


print("""Welcome to my calculator!
In order to use it, you need to separate the numbers and arithmetic symbols with a single space like this - X + Y or 
(X - Y). Otherwise it will explode. Currently, it only supports addition, subtraction, multiplication and division.
If you find bugs, message me.""")
equation = input("Type your expression here: ")

equation = bracket_solving(equation)

equation = multiplication(equation)

equation = division(equation)

equation = addition(equation)

equation = subtraction(equation)

print(f"Result: {equation.rstrip('0').rstrip('.') if equation != '0' else '0'}")
