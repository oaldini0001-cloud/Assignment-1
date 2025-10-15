

while True:
 print("Welcome to Multi-Mode Calculator\n1. Standerd Mode \n2. Programmer Mode \n3. Scientific Mode \n4. Converter Mode \n5. Exit ")
 try:
    Choice=int(input('Enter your choice: '))
    if Choice==1:
         print('Standerd Mode')
    elif Choice==2:
         print("Programmer Mode") 
    elif Choice==3:
          import scientific
    elif Choice==4:
         print("Converter Mode")
    elif Choice==5:
         break
    elif 5<Choice or Choice<1:
         print("Value Error , Please enter a valid number (1-5)")
    
 except ValueError:
     print("Error, Please enter a valid number ")