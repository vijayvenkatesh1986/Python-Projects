
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(weight)/(float(height) * float(height))
print("Your BMI is {}".format(round(bmi,2)))