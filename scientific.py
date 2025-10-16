import math
def val():

    while True :
        try:
            value = float(input("Enter value"))
        except Exception:
            print("Please enter numeric values.")
            continue
        else:
            break
    return value

def radians_degrees_conversion():

    degree_or_radians = input("Enter r to convert from degree to radians, or d to convert from radian to degree: ")
    while True:
        if degree_or_radians.strip().lower() == "r" or degree_or_radians.strip().lower() == "d":
            break
        print("Wrong input, Enter again: d or r ")
        degree_or_radians = input("Enter d to convert from degree to radians, or r to convert from radian to degree: ")       

    value = val()
    
    if degree_or_radians.strip().lower() == "r" :
        value = math.radians(value)
    else :
        value = math.degrees(value)
    return value

def radians_degrees():
    degree_or_radians = input("degree or radian? ")
    while True :
        if degree_or_radians.strip().lower() == "radian":
            break
        elif degree_or_radians.strip().lower() == "degree" :
            break
        print("Wrong input, Enter again : degree or radian ")
        degree_or_radians = input("degree or radian? ")

    value = val()

    if degree_or_radians.strip().lower() == "degree":
       value = math.radians(value)
    return value
      
def sin():
    return math.sin(radians_degrees())
def cos():
    return math.cos(radians_degrees())
def tan():
    angle = math.degrees(radians_degrees())
    while angle % 180 == 90:
        print("wrong angle, try again")
        angle = math.degrees(radians_degrees())
    return math.tan(math.radians(angle))

def asin():
    value = val()
    while  value < -1 or value > 1:
        print("wrong value, enter between the range 1 and -1")
        value = val()
    return math.asin(value)
def acos():
    value = val()
    while  value < -1 or value > 1:
        print("wrong value, enter between the range 1 and -1")
        value = val()
    return math.acos(value)
    
def atan():
    return math.atan(val())

def pi():
 return math.pi

def factorial():
    value = val()
    while value < 0 or int(value) != value:
        print("Wrong value: enter a non-negative integer")
        value = val()
    return math.factorial(int(value))

def e_constants():
    return math.exp(1)
def log():
    value = val()
    while value <= 0:
        print("Error: Logarithm undefined for non-positive numbers.")
        value = val()
    return math.log10(value)
def ln():
    value = val()
    while value <= 0:
        print("Error: Natural log undefined for non-positive numbers.")
        value = val()
    return math.log(value)
def exp():
    while True:
      try:
        value = val()
        n = math.exp(value)
      except OverflowError :
        print("Value too large. Try a smaller number.")
        continue
      else:
            break
    return n

def sinh():
    while True:
        try:
            value = val()
            n = math.sinh(value)
        except OverflowError :
             print("Value too large. Try a smaller number.")
             continue
        else:
            break
    return n
def tanh():
    while True:
        try:
            value = val()
            n = math.tanh(value)
        except OverflowError :
             print("Value too large. Try a smaller number.")
             continue
        else:
            break
    return n
def cosh():
    while True:
        try:
            value = val()
            n = math.cosh(value)
        except OverflowError :
             print("Value too large. Try a smaller number.")
             continue
        else:
            break
    return n

def x(choice):
    return choice.strip().lower()

def main_menu() :
  while True:
    print("Scientific Mode ")
    print("Enter one of these function: ")
    print("sin, cos, tan, arcsin, arccos, arctan, pi, e, sinh, cosh, tanh, exp, ln, log, factorial")
    choice = input("Enter function, Enter exit to exit:  ")
    
    if x(choice) == "sin":
        a = sin()
    elif x(choice) == "cos":
        a = cos()
    elif x(choice) == "tan":
        a = tan()
    elif x(choice) == "arcsin":
        a = asin()
    elif x(choice) == "arccos":
      a = acos()
    elif x(choice) == "arctan":
        a = atan()
    elif x(choice) == "pi":
        a = pi()
    elif x(choice) == "e":
        a = e_constants()
    elif x(choice) == "sinh":
        a = sinh()
    elif x(choice) == "cosh":
        a = cosh()
    elif x(choice) == "tanh":
        a = tanh()
    elif x(choice) == "exp":
        a = exp()
    elif x(choice) == "ln":
        a = ln()
    elif x(choice) == "log":
        a = log() 
    elif x(choice) == "factorial":
        a = factorial() 
    elif x(choice) == "exit":
        print("Returning to Main Menu...")
        break
    else:
         print("WRONG INPUT")
         continue
    print("Result:", round(a, 4))



main_menu() 