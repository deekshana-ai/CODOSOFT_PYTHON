print("=" * 40)
print( " CODESOFT CALCULATOR")
print("=" * 40)
print("\nChoose an operation:")
print("1. Addition(+)")
print("2. Subtraction(-)")
print("3. Multiplication(*)")
print("4. Division(/)")
choice = input("\nEnter your choice (1-4):")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice=="1":
    print("Result=",num1 + num2)
elif choice=="2":
    print("Result=",num1 - num2)
elif choice=="3":
    print("Result=",num1 * num2)
elif choice=="4" :
    if num2!=0:
        print("Result=",num1 / num2)
    else:
        print("Error!  Division by Zero is not Allowed.")
else:
    print("Invalid choice")