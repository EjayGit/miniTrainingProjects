height = float(input("Enter your height in m: "))
weight =  float(input("Enter your weight in kg: "))
# TODO
BMI = round(weight/(height**2),1)
print(f"Your BMI is {BMI}. You are: ")
if BMI<18.5:
    print("underweight")
elif BMI<25:
    print("normal")
elif BMI<30:
    print("overweight")
else:
    print("obese")