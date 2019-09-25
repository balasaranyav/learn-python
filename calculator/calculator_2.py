def add(x, y):
  return x + y
def subtract(x, y):
  return x - y
def multiply(x, y):
  return x * y
def divide(x, y):
  return x / y
def modulo(x,y):
  if y!=0:
    return x % y
  else:
    return print("Infinity")
while(1):
  print("-----SIMPLE CALCULATOR-----")
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))
  print("---Select operation---")
  print("1.Add")
  print("2.Subtract")
  print("3.Multiply")
  print("4.Divide")
  print("5.Modulo division")
  choice = input("Enter your choice(1/2/3/4/5):")
  if choice == '1':
    print("Addition of two numbers is")
    print(num1,"+",num2,"=", add(num1,num2))
  elif choice == '2':
    print("Subtraction of two numbers is")
    print(num1,"-",num2,"=", subtract(num1,num2))
  elif choice == '3':
    print("Multiplication of two numbers is")
    print(num1,"*",num2,"=", multiply(num1,num2))
  elif choice == '4':
    print("Division of two numbers is")
    print(num1,"/",num2,"=", divide(num1,num2))
  elif choice == '5':
    print("Modulo division of two numbers is")
    print(num1,"%",num2,"=",modulo(num1,num2))
  else:
    print("Please enter the valid input")
  stop = input("Do you want to continue?(y/n): ")
  if stop == 'n':
    break