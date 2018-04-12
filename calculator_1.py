print()
print()
print()
print("CALCULATOR 1.0")
print()
print()
while True:
	print("The following calculator is based on two variables only.")
	print()
	print()
	print("Options:")
	print()
	print("Enter 'add' for addition")
	print("Enter 'subtract' for subtraction")
	print("Enter 'multiply' for mutltiplication")
	print("Enter 'divide' for division")
	print("Enter 'quit' to exit calculator")
	user_input = input(":")

	if user_input == "quit":
		break
	elif user_input == "add":
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))
		res = str(num1+num2)
		print('The sum of ' + str(num1) + ' plus ' + str(num2) + ' is ' + res + """
*********************************************************
""")
	elif user_input == "subtract":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                res = str(num1-num2)
                print("The difference of " + str(num1) + " minus " + str(num2) + " is " + res + """
*********************************************************
""")
	elif user_input == "multiply":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                res = str(num1*num2)
                print("The product of " + str(num1) + " times " + str(num2) + " is " + res + """
********************************************************
""")
	elif user_input == "divide":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                res = str(num1/num2)
                print("The quotient of " + str(num1) + " divided by " + str(num2) + " is " + res + """
*********************************************************
""")
	else:
		print("Unknown input"+"""
*********
*********""")

