def bmi(we,he):
    bmi=we/(he*he)
    print(f"Your BMI = {bmi}")

we=float(input("Enter your Weight in Kilograms = "))
he=float(input("Enter your Height in Meters = "))
bmi(we,he)
