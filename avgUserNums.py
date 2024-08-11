# TODO
def intCheck(num):
    try:
        num = float(num)
        return num
    except (ValueError, TypeError):
        print("Error, please enter numeric input")
        return False

count = 0
total = 0.0
average = 0.0

while True:
    number = input("Enter a number: ")
    if number == 'done':
        break
    ans = intCheck(number)
    if not ans:
        continue
    count += 1
    total = total + ans

if count != 0:
    average = total / count
    
print(total, count, average)
