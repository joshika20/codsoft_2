def calculator():
 num1= float(input("Enter a first number:"))
 num2=float(input("Enter a second number:"))
 print("choose an operation from below")
 print("1-Addition(+)")
 print("2-Subtraction(-)")
 print("3-Multiplication(*)")
 print("4-Division(/)")
 print("5-Floor division(//)")
 print("6-Modulus(%)")
 print("7-Exponentiation(**)")
 operation=input("Enter the number (or) operator corresponding to the operation:")
 if (operation=='1' or operation== '+'):
     result=num1+num2
     return
 elif(operation=='2'or operation=='-'):
     result=num1-num2
     
 elif(operation=='3'or operation=='*'):
     result=num1*num2
     
 elif(operation=='4'or operation=='/'):
     if num2!=0:
        result=num1/num2
     else:
          print("Error: division by zero is not allowed")
     
 elif(operation=='5'or operation=='//'):
     if num2!=0:
        result=num//2
     else:
         print("Error: division by zero is not allowed")
     
 elif(operation=='6'or operation=='%'):
     if num2!=0:
        result=num%2
     else:
         print("Error: division by zero is not allowed")
     
 elif(operation=='7'or operation=='**'):
       result=num**2
       
 else:
    print("Invalid  operator.Please select a valid operator")
    return
 print("Result",result)
calculator()
    
