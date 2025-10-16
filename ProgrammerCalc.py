#This mode focuses on operations useful for programmers, including base conversions and bitwise operations.

def programmerMode():
    while True:
        print("\n \nProgrammer Mode")
        print("choose the conversions type:")
        print("1. from decimal to other units")
        print("2. from other units to decimal")
        print("3. bitwise conversions")
        print("4. Exit")

        choice = input("enter your choice (1,2,3,4): ")

        if choice not in ["1", "2", "3", "4"]:
            print("wrong choice, please try again using (1,2,3,4)")
# if the user entered a wrong input the action will skip the rest of the loop and retry and if he but a right input we move to next step
            continue

        if choice == "4":
            return

#the first choice is to change from a decimal unit to other units ( all of the units will apear )

#in python if we do not add [2:], for example in binary the program will print it (0b...). so we add it to remove it           
        
        if choice == "1":
            while True:
# we try these comands if one is not right we print the except print and return the loop with continue 
                try:
                    deci = int(input("\nenter the decimal number: "))
                    print("in binary      :", bin(deci)[2:])
                    print("in octal       :", oct(deci)[2:])
                    print("in hexadecimal :", hex(deci)[2:].upper())
                    break  
                except:
                    print(" wrong input, please enter an integer")
                    continue

#the second choice is to change from other units to decimal ( the program will give the option to select the unit you want )
        
        elif choice == "2":
            while True:
                print("\nchoose the base:")
                print("1. binary")
                print("2. octal")
                print("3. hexadecimal")
                base_choice = input("enter your choice (1,2,3): ")

                if base_choice not in ["1", "2", "3"]:
                    print("invalid choice, please try again using (1,2,3)")
                    continue

                num = input("enter the number : ")
# this is how we convert any base to a decimal number wether its binary(base(2)) or octal(base(8)) or hexadecimal(base(16))

# we put int(num, base) to converrt it
                try:
                    if base_choice == "1":
                        print("decimal:", int(num, 2))
                    elif base_choice == "2":
                        print("decimal:", int(num, 8))
                    elif base_choice == "3":
                        print("decimal:", int(num, 16))
                    break  
                except:
                    print("wrong choice, please enter a valid number for the base")
                    continue

#the third choice for the bitwise operation (6 bitwise operation to choose from )

        elif choice == "3":
            while True:
                print("\nchoose the bitwise operation:")
                print("1. and")
                print("2. or")
                print("3. xor")
                print("4. not")
                print("5. left shift")
                print("6. right shift")
                op_choice = input("enter your choice : ")

# the bitwise operation get the binary of a certain number and compare it with an another one in any formatt (and,or,xor,...etc)
                try:
                    if op_choice in ["1", "2", "3", "5", "6"]:
                        a = int(input("enter the first number: "))
                        b = int(input("enter the second number: "))
                        if op_choice == "1":
                            print("result is:", a & b)
                        elif op_choice == "2":
                            print("result is:", a | b)
                        elif op_choice == "3":
                            print("result is:", a ^ b)
                        elif op_choice == "5":
                            print("result is:", a << b)
                        elif op_choice == "6":
                            print("result is:", a >> b)
                        break
# the not is alone in here because it only take one value and revert it. for example a binary is 110 its ~ is 001
                    elif op_choice == "4":
                        a = int(input("enter number: "))
                        print("result is:", ~a)
                        break  
                    else:
                        print(" wrong choice, please try again using (1-6)")
                        continue
                except:
                    print("wrong input, please enter an integer")
                    continue


