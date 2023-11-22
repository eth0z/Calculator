def Calculator():
  op = input("Enter operation. (+ - / *) > ") ## Gets the operation being used. ##
  num1 = input("Enter first number > ") ## Gets the first number ##
  try:
    num1 = int(num1)
    num2 = input("Enter second number > ") ## Gets the second number ##
    try:
      num2 = int(num2) 
      if op == "+":
        print(f"The answer is {num1 + num2}.") ## Prints answer ##
      elif op == "-":
        print(f"The answer is {num1 - num2}.") ## Prints answer ##
      elif op == "*":
        print(f"The answer is {num1 * num2}.") ## Prints answer ##
      elif op == "/":
        if num2 == "0":
          print("Error: Cannot divide by 0.") ## Screams at you for dividing by zero ##
          Calculator()
        else:
          print(f"The answer is {num1 / num2}.") ## Prints answer ##
      else:
          print("Invalid operation. ") ## Screams at you if operation is not +, -, * or / ##
      Calculator()
    except ValueError:
      print("Error: Value must be a number.") ## Why are you trying to use strings in a calculator? ##
      Calculator()
  except ValueError:
    print("Error: Value must be a number.") ## Why are you trying to use strings in a calculator? ##
    Calculator()
Calculator()
