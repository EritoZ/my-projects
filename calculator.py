import re
from decimal import Decimal


def get_first_num(sub_or_full_expression, index):
    num = []
    start = 0

    for i in range(index - 1, -1, -1):

        if sub_or_full_expression[i] == " ":
            start = i + 1
            break

        num.append(sub_or_full_expression[i])

    num = ''.join(num[::-1])

    return Decimal(num), start


def get_second_num(sub_or_full_expression, index):
    num = []
    end = len(sub_or_full_expression)

    for i in range(index + 3, end):

        if sub_or_full_expression[i] == " ":
            end = i
            break

        num.append(sub_or_full_expression[i])

    num = ''.join(num)

    return Decimal(num), end


def addition(sub_or_full_expression):
    while " + " in sub_or_full_expression:
        plus_location = sub_or_full_expression.index(" + ")

        first_num, start = get_first_num(sub_or_full_expression, plus_location)
        second_num, end = get_second_num(sub_or_full_expression, plus_location)

        result = (first_num + second_num).normalize()

        sub_or_full_expression = sub_or_full_expression[:start] + str(result) + sub_or_full_expression[end:]

    return sub_or_full_expression


def subtraction(sub_or_full_expression):
    while " - " in sub_or_full_expression:
        minus_location = sub_or_full_expression.index(" - ")

        first_num, start = get_first_num(sub_or_full_expression, minus_location)
        second_num, end = get_second_num(sub_or_full_expression, minus_location)

        result = (first_num - second_num).normalize()

        sub_or_full_expression = sub_or_full_expression[:start] + str(result) + sub_or_full_expression[end:]

    return sub_or_full_expression


def multiplication(sub_or_full_expression):
    while " * " in sub_or_full_expression:
        multiplication_location = sub_or_full_expression.index(" * ")

        first_num, start = get_first_num(sub_or_full_expression, multiplication_location)
        second_num, end = get_second_num(sub_or_full_expression, multiplication_location)

        result = (first_num * second_num).normalize()

        sub_or_full_expression = sub_or_full_expression[:start] + str(result) + sub_or_full_expression[end:]

    return sub_or_full_expression


def division(sub_or_full_expression):
    while " / " in sub_or_full_expression:
        division_location = sub_or_full_expression.index(" / ")

        first_num, start = get_first_num(sub_or_full_expression, division_location)
        second_num, end = get_second_num(sub_or_full_expression, division_location)

        result = first_num / second_num

        sub_or_full_expression = sub_or_full_expression[:start] + str(result) + sub_or_full_expression[end:]

    return sub_or_full_expression


def bracket_solving(the_expression):
    while "(" in the_expression or ")" in the_expression:

        if "(" in the_expression and ")" in the_expression:
            bracket_expression = re.search(r"\(([^(]+?)\)", the_expression)

            bracket_expression_start = bracket_expression.start()
            bracket_expression_end = bracket_expression.end()

            bracket_expression = bracket_expression.group(1)

            bracket_expression = multiplication(bracket_expression)

            bracket_expression = division(bracket_expression)

            bracket_expression = addition(bracket_expression)

            bracket_expression = subtraction(bracket_expression)

            the_expression = the_expression[:bracket_expression_start] + bracket_expression \
                             + the_expression[bracket_expression_end:]

        else:
            raise SyntaxError("Error, invalid syntax.")

    return the_expression


print("""Welcome to my calculator!
In order to use it, you need to separate the numbers and arithmetic symbols with a single space like this - A + B or 
(A - B). Otherwise it will explode. Currently, it only supports addition, subtraction, multiplication and division.
If you find bugs, message me.\n""")

while True:
    expression = input("Type your expression here: ")

    expression = bracket_solving(expression)

    expression = multiplication(expression)

    expression = division(expression)

    expression = addition(expression)

    expression = subtraction(expression)

    print(f"Result: {expression}\n")
