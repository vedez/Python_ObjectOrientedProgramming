# Description:
# Asking user to input height and weight then calculating BMI.
# Taking input in pounds and converting into metric measurements.

# Taking height and weight input
weight_pounds = float(input("Please input your weight (Pounds): "))

print("Please input your height (Ft, In): ")
height_feet = float(input("Feet: "))
height_inches = float(input("Inches: "))

# Converting pounds into kilograms and inches into meters
height_inches += (height_feet * 12)
height_meters = height_inches * 0.0254
weight_kg = weight_pounds * 0.453592

# Calculating BMI
# Formula: ( weight (kg) / height (metric) ^ 2
bmi = weight_kg / (height_meters ** 2)

print("Your BMI is : ", round(bmi, 2))


