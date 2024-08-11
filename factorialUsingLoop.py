import math

def factorial(p_num):
    # TODO
    if p_num < 0:
        return "Factorial does not exist for negative numbers"
    elif p_num == 0:
        return "The factorial of 0 is 1"
    else:
        ans = math.factorial(p_num)
        return f"The factorial of {p_num} is {ans}"
   