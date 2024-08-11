height = float(input("Enter your height in m: "))
weight =  float(input("Enter your weight in kg: "))
# TODO
BMI = round(weight/(height**2),2)
if BMI<18.5:
    print(f"Your bmi is {BMI}, you are underweight.")
elif BMI<25:
    print(f"Your bmi is {BMI}, your weight is normal.")
elif BMI<30:
    print(f"Your bmi is {BMI}, you are overweight.")
else:
    print(f"Your bmi is {BMI}, you are obese.")