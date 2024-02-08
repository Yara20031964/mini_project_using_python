num1=float(input("Please enter the frist number: "))
num2=float(input("Please enter the secound number: "))
op=input("Select the operation that you want to do in this two number: ")
if op=='+':
    print((num1)+(num2))
elif op=='-':
    print((num1)- (num2))
elif op=='*':
    print((num1)*(num2))
elif op=='/':
    print((num1)/(num2))
elif op=='^':
    print((num1)**(num2))
else:
    print("Invalid operator")
