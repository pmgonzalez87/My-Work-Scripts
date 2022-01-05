# CALCULATE BMI

def calculateBMI(w, h):
    # two constants
    KILOS_PER_POUND = 0.4536 # constants
    METERS_PER_INCH = 0.0254 # constants

    #computer BMI
    weightInKilos = w * KILOS_PER_POUND
    heightInMeters = h * METERS_PER_INCH
    bmi = weightInKilos / (heightInMeters * heightInMeters)

    return bmi

   
    #end of function printBMIDetails()

weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))

result = calculateBMI(weight, height)
print("BMI is", result)
print()
#Display your shape
if result < 18.5:
    print("Underweight")
elif result < 25:
    print("Normal")
elif result < 30:
    print("Overweight")
else:
    print("Obese")

