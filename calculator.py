import re
from decimal import Decimal


def get_first_num(sub_or_full_expression, index):
    num = ""
    start = 0

    for i in range(index - 1, -1, -1):
        if sub_or_full_expression[i] != " " and sub_or_full_expression[i] != "(":
            num += sub_or_full_expression[i]
            if i == 0:
                start = i
        else:
            start = i + 1
            break

    return Decimal(num[::-1]), start


def get_second_num(sub_or_full_expression, index):
    num = ""
    end = 0

    for i in range(index + 3, len(sub_or_full_expression)):
        if sub_or_full_expression[i] != " " and sub_or_full_expression[i] != ")":
            num += sub_or_full_expression[i]
            if i == len(sub_or_full_expression) - 1:
                end = i + 1
        else:
            end = i
            break

    return Decimal(num), end


def addition(sub_or_full_expression):
    while " + " in sub_or_full_expression:
        plus_location = sub_or_full_expression.index(" + ")
        
        first_num, start = get_first_num(sub_or_full_expression, plus_location)
        second_num, end = get_second_num(sub_or_full_expression, plus_location)
        
        result = str(first_num + second_num)

        sub_or_full_expression = sub_or_full_expression[:start] + result + sub_or_full_expression[end:]

    return sub_or_full_expression


def subtraction(sub_or_full_expression):
    while " - " in sub_or_full_expression:
        minus_location = sub_or_full_expression.index(" - ")
        
        first_num, start = get_first_num(sub_or_full_expression, minus_location)
        second_num, end = get_second_num(sub_or_full_expression, minus_location)
        
        result = str(first_num - second_num)

        sub_or_full_expression = sub_or_full_expression[:start] + result + sub_or_full_expression[end:]

    return sub_or_full_expression


def multiplication(sub_or_full_expression):
    while " * " in sub_or_full_expression:
        multiplication_location = sub_or_full_expression.index(" * ")
        
        first_num, start = get_first_num(sub_or_full_expression, multiplication_location)
        second_num, end = get_second_num(sub_or_full_expression, multiplication_location)
        
        result = str(first_num * second_num)

        sub_or_full_expression = sub_or_full_expression[:start] + result + sub_or_full_expression[end:]

    return sub_or_full_expression


def division(sub_or_full_expression):
    while " / " in sub_or_full_expression:
        division_location = sub_or_full_expression.index(" / ")
        
        first_num, start = get_first_num(sub_or_full_expression, division_location)
        second_num, end = get_second_num(sub_or_full_expression, division_location)
        
        result = str(first_num / second_num)

        sub_or_full_expression = sub_or_full_expression[:start] + result + sub_or_full_expression[end:]

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
If you find bugs, message me.""")

expression = input("Type your expression here: ")

expression = bracket_solving(expression)

expression = multiplication(expression)

expression = division(expression)

expression = addition(expression)

expression = subtraction(expression)

print(f"Result: {expression.rstrip('0').rstrip('.') if expression != '0' else '0'}")
