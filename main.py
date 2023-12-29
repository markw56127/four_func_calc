from art import logo

print(logo)

def add(a,b):
  return a + b

def sub(a,b):
  return a - b

def mult(a,b):
  return a * b

def div(a,b):
  return a / b

calc_dict = {"+":add,"-":sub,"*":mult,"/":div}

def calculator():
  num1 = float(input("What is your first number? "))
  num2 = float(input("What is your second number? "))
  for i in calc_dict:
    print(i)
  choice = input("Pick an operation from the line above: ")
  ans = calc_dict[choice](num1,num2)
  print(f"{num1} {choice} {num2} = {ans}")
  
  cont = True
  while cont == True:
    yn = input(f"Type 'yes' to continue calculating with {ans}, type 'no' to calculate with a new number, or type 'quit' to quit the program.\n")
    if yn == 'quit':
      cont = False
    elif yn == 'no':
      calculator()
      break
    elif yn == 'yes':
      choice = input("Pick an operation: ")
      num3 = float(input("What's the next number? "))
      prev_ans = ans
      ans = calc_dict[choice](ans,num3)
      print(f"{prev_ans} {choice} {num3} = {ans}")

calculator()
