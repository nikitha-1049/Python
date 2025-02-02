iter=1
while(iter):
    num1=int(input("Enter number1:"))
    num2=int(input("Enter number2:"))
    print("Select your operation")
    print("1.Add\n2.Sub\n3.Mul\n4.Div\n5.mod")
    option=int(input())
    if(option==1):
        print(f"The sum of {num1} and {num2} is :{num1+num2}") 
    elif(option==2):
        print(f"The subtraction of {num1} and {num2} is :{num1-num2}") 
    elif(option==3):
        print(f"The product of {num1} and {num2} is :{num1*num2}") 
    elif(option==4):
        print(f"The division of {num1} and {num2} is :{num1/num2}") 
    else:
        print(f"The modulus of {num1} and {num2} is :{num1%num2}") 
    print("if u want more caliculation enter 1 or 0 to exit")
    iter=int(input())
