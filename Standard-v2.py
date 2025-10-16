import math

def StandarD():
    while True:
        print("~~~~~ Standard Calculator ~~~~~")
        print("| (1) Addition                |")
        print("| (2) Subtraction             |")
        print("| (3) Multiplication          |")
        print("| (4) Division                |")
        print("| (5) Square Root             |")
        print("| (6) Reciprocal              |")
        print("| (7) Percentage              |")
        print("| (8) Exponentiation          |")
        print("| (9) Modulo                  |")
        print("| (10) Back to Main Menu      |")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        try:
            choice = input("Choose an operation (1-10): ")

            if choice == '10':
                break

        
            #Square Root
            if choice == '5':
                while True:
                    try:
                        num = float(input("Enter number: "))

                        if num < 0:
                            print("Error: cannot take square root of negative number.")
                        else:
                            print("Result =", math.sqrt(num))
                            break  
                    except:
                        print("Error: please enter valid numbers.")
                   
            #Reciprocal
            elif choice == "6":
                while True:
                    try:
                        num = float(input("Enter number: "))
                        if num == 0:
                            print("Error: cannot divide by zero.")
                            
                        else:
                            print("Result =", 1 / num)
                            break
                    except:
                        print("Error: please enter valid numbers.")
            #Modulo
            elif choice == "9":
                while True:
                    try:
                        num1 = float(input("Enter first number: "))
                        num2 = float(input("Enter second number: "))
                        if num2 == 0:
                            print("Error: cannot divide by zero.")
                            
                        else:
                            print("Result =", num1 % num2)
                            break
                    except:
                        print("Error: please enter valid numbers.")
                      
            #Percentage
            elif choice == "7":
                while True:
                 try:
                    num1 = float(input("Enter The number of Percentage:  "))
                    num2 = float(input("Enter number: "))
                    break
                 except:
                      print("Error: please enter valid numbers.")
                print("Result =", (num1/100)*num2)
                
            #Division
            elif choice == '4':
                while True:
                    try:
                        num1 = float(input("Enter first number: "))
                        num2 = float(input("Enter second number: "))
                        
                        if num2 == 0:
                            print("Error: cannot divide by zero.")
                        
                        else:   
                            print("Result =", num1 / num2)
                            break
                    except:
                        print("Error: please enter valid numbers.")
                        
                
            elif choice in ("1","2","3","8"):
                while True:
                 try:
                     num1 = float(input("Enter first number: "))
                     num2 = float(input("Enter second number: "))
                     break
                 except:
                      print("Error: please enter valid numbers.")
                #Addition
                if choice == '1':
                    print("Result =", num1 + num2)
                    
                #Subtraction
                elif choice == '2':
                    print("Result =", num1 - num2)
                
                #Multiplication
                elif choice == '3':
                    print("Result =", num1 * num2)
                    
                #Exponentiation        
                elif choice == "8":
                    print("Result =", num1 ** num2)
                    
                    
            else:
                print("Invalid choice.")
                    
        except:
            print("Error: please enter valid numbers.")
            
            
StandarD()
