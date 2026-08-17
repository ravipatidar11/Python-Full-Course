#program for Implementation Temp Conversion Scale
#MatchCaseEx2.py

s="""
===================================================
	Temperature Conversion Scale
===================================================
        1. F to C
        2. F to K
        3. C to F
        4. C to K
        5. K to F
        6. K to C
        7. Exit
==================================================="""

print(s)

ch=float(input("Enter your choice: "))

match ch:
    case 1:
        F = float(input("Enter Temperature in Fahrenheit: "))
        C = (F-32)*(5/9)
        print("Temperature in Celsius is ",C)
    case 2:
        F = float(input("Enter Temperature in Fahrenheit: "))
        K = (F - 32) * (5 / 9) + 273.15
        print("Temperature in Kelvin is ", K)
    case 3:
        C = float(input("Enter Temperature in Celsius: "))
        F = C*(9/5)+32
        print("Temperature in Fahrenheit is ", F)
    case 4:
        C = float(input("Enter Temperature in Celsius: "))
        K = C + 273.15
        print("Temperature in Kelvin is ", K)
    case 5:
        K = float(input("Enter Temperature in Kelvin: "))
        F = (K - 273.15)*(9/5)+32
        print("Temperature in Fahrenheit is ", F)
    case 6:
        K = float(input("Enter Temperature in Kelvin: "))
        C = K - 273.15
        print("Temperature in Celsius is ", C)
    case 7:
        print("Program Completed")
        exit()
    case _:
        print("Invalid Input --- Try Again")