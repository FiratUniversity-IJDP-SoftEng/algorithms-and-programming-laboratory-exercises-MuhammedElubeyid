# Your Student ID:220543603
# Your Name and Surname: Muhammed Elubeyid
flag= True
while flag:
 num1= float(input("Please enter the first number: "))
 num2= float(input("Please enter the second number: "))
 operation= input("Enter one of this operations(+, -, *, /): ")

 if operation=='+':
     print(num1+ num2)
 elif operation=='-':
     print(num1- num2)
 elif operation=='*':
     print(num1* num2)
 elif operation=='/':
      if num2== 0:
          print("Error! Cannot divided by 0")
      else:
          print(num1/ num2)
 else:
     print("Invalid input")
 check=input("If you want to perform another calculation enter yes: ").lower()
 if check!='yes':
     flag= False
