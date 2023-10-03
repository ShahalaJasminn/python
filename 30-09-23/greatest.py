num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
if(num1>=num2)&(num1>=num3):
    print("largest is ",num1)
elif(num2>=num1)&(num2>=num3):
       print("largest is",num2)
else:
    print("largest is ",num3)
