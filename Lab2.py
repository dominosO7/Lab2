def calculate_bmi(height, weight):
    bmi=weight/height**2
    print("Height =",height)
    print("Weight =",weight)
    print("bmi is ",bmi)
    return bmi

def classify_bmi(bmi):
    if(bmi>=30.0):
        returnvalue = 0
        print("Obese")
    elif(bmi<30.0 and bmi>25.0):
        returnvalue = 1
        print("Overweight")
    elif(bmi>=18.5 and bmi<=25.0):
        returnvalue = -1
        print("Underweight")
    else:
        print("Impossible BMI")

    return returnvalue

def app():
    output = calculate_bmi(1.79,50.0)
    returnvalue = classify_bmi(output)
    print("return value =", returnvalue)
    return
if __name__ == "__main__":
    app()
