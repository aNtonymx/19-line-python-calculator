n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
process = input("Enter process: ")
if process == "+":
    print(n1 + n2)
elif process == "-":
    print(n1 - n2)
elif process == "*":
    print(n1 * n2)
elif process == "/":
    print(n1 / n2)
elif process == "%":
    print(n1 % n2)
elif process == "**":
    print(n1 ** n2)
elif process == "//":
    print(n1 // n2)
else:
    print("Invalid process")