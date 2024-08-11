def check_for_float(p_input):
    try:
        val = float(p_input)
        return val
    except (ValueError, TypeError):
        print("Error, please enter numeric input")
        return False

# TODO
count = 0
max = 0.0
min = 0.0

while True:
    number = input("Enter a number: ")
    if number == 'done':
        print("number")
        break
    ans = check_for_float(number)
    if not ans:
        print(ans)
        continue
    if count == 0:
        min = ans
        max = ans
    if ans > max:
        max = ans
    if ans < min:
        min = ans
    count += 1
    
print(f"Maximum number: {max}, Minimum number: {min}")