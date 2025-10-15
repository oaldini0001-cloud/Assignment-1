## converter mode  
   # This mode handles unit conversions across categories
      
def converter_length():
   print("--- Length Conversion ---")
   len_factors={"m": 1.0 ,"cm": 0.01 ,"ft": 0.3048 ,"in": 0.0254}

   while True:
    from_unit=input("From unit (m,cm,ft,in): ").strip().lower()
    if from_unit in len_factors:
      break
    else:
       print("Error You mest be choice only: m, cm, ft, in ")
   while True:
      to_uint=input("To unit (m,cm,ft,in): ").strip().lower()
      if to_uint in len_factors:
         break
      else:
         print("Error You mest be choice only: m, cm, ft, in ")
      

   try:
      Value= float(input("Enter the number: "))

      if Value < 0 :
         print("Error length cannot be negative")
         return
      meter= Value* len_factors[from_unit]
      result= meter / len_factors[to_uint]
      print("Result", round(result,2),to_uint)
   except ValueError:
      print("Error: Please enter a valid number") 


def converter_Weight() :
   print("--- Weight Conversion ---")
   weight_factors={"kg": 1.0 ,"g": 0.001 ,"lb": 0.45359 ,"oz": 0.02834}

   while True:
    from_unit=input("From unit (Kg,g,lb,oz): ").strip().lower()
    if from_unit in weight_factors:
       break 
    else:
       print("Error You mest be choice only: kg, g, lb, oz")
   while True:
     to_unit=input("To unit (Kg,g,lb,oz): ").strip().lower()
     if  to_unit in weight_factors :
        break
     else:
        print("Error You mest be choice only: Kg, g, lb, oz")
   
   
   try:
      Value= float(input("Enter the number: "))

      if Value < 0 :
         print("Error Weight cannot be negative")
         return
      Kilogram= Value* weight_factors[from_unit]
      result= Kilogram / weight_factors[to_unit]
      print("Result", round(result,2),to_unit)
   except ValueError:
      print("Error: Please enter a valid number") 

def converter_temperature():
   print("--- Temperature Conversion ---")
   Valid =("C","K","F")

   while True:
      from_unit=input("From unit (C, K, F): ").strip().upper()
      if from_unit in Valid:
         break
      else:
         print("Error You mest be choice (C, K, F).") 
   while True:
      to_unit=input("From unit (C, K, F): ").strip().upper()
      if to_unit in Valid:
         break
      else:
         print("Error You mest be choice (C, K, F).")
   
   try:
      Value=float(input("Enter the number: "))

      if from_unit=="C":
         if to_unit=="F":
            result= (Value * 9/5)+32
         else:
             result= Value+273.15
      elif from_unit=="F":
         if to_unit=="C":
            result= (Value - 32)*5/9
         else:
             result= ((Value - 32)*5/9)+273.15
      elif from_unit=="K":
         if to_unit=="C":
            result= Value - 273.15 
         else:
             result= ((Value - 273.15)*9/5)+32
      else:
         print("Error You mest be choice (C, K, F).")

      print("Result",round(result,2),to_unit)
   except ValueError:
      print("Error: Please enter a valid number")


while True:
    print("---Converter Mode ---")
    print("1-Length")
    print("2-Weight")
    print("3-Temperature")
    print("4-Back to main")

    choice=input("Enter your choice: ")

    if choice=="1":
      print(" Your choice Length")
      converter_length()
    elif choice=="2":
      print("Your choice Weight")
      converter_Weight() 
    elif choice=="3":
       print("Your choice Temperature")
       converter_temperature()
    elif choice=="4":
       print("return to mian ")
       break
    else:
       print("Invalid choice ,Please try again.")
       
