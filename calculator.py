def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b ==0 :
        return "error cannot divide by zero"
    return a/b

num1 = float(input("Enter first number: "))
print("choose operation:add,sub,mul,div")
op = input("operation")
num2 = float(input("Enter second number: "))     
if op =="add":
    result =(add(num1,num2))
elif op =="sub":
    result = sub(num1,num2)
   
elif op =="mul":
    result = mul(num1,num2)
    
elif op =="div":
    result = (div(num1,num2))  

else :
    print("invalid operation")     
print(result)    


print("result of first operation is:",result)
choice = input("do you want to perform another operation on the result? (yes/no): ")
if choice == "yes":
    print("choose operation:add,sub,mul,div")
    op2 = input("operation")
    num3 = float(input("Enter another number: "))
    if op2 =="add":
     
     print(add(result,num3))
    elif op2 =="sub":

        print(sub(result,num3))

    elif op2 =="mul":
        print(mul(result,num3))
    elif op2 =="div":
        print(div(result,num3))  

else :
    print("invalid operation")





