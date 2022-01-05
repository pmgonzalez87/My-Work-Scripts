# CALCULATE BMI

def printBMIDetails(w, h):
    # two constants
    KILOS_PER_POUND = 0.4536 # constants
    METERS_PER_INCH = 0.0254 # constants

    #computer BMI
    weightInKilos = w * KILOS_PER_POUND
    heightInMeters = h * METERS_PER_INCH
    bmi = weightInKilos / (heightInMeters * heightInMeters)

    print("BMI is", bmi)

    #Display your shape
    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal")
    elif bmi < 30:
        print("Overweight")
    else:
        print("Obese")

    #end of function printBMIDetails()

weight = eval(input("Enter your weight in pounds: "))
height = eval(input("Enter your height in inches: "))

printBMIDetails(weight, height)

