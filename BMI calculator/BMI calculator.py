while True:
    weight = float(input("Enter your weight, Kg:"))
    height = float(input("Enter your height, Meter:"))
    Total = weight/(height**2/10000)
    print("This is your BMI:", Total, "\n")
