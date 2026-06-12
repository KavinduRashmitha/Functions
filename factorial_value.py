"***This is a Function to Find Factorial***"
#ForLoop
def Factorial(n):
    tot=1
    for i in range(n,1,-1):
        tot=tot*i
    return tot

#WhileLoop
def Factorial_While(n):
    tot=1
    count=2
    while count<=n:
        tot=tot*count
        count+=1
    return tot

num=int(input("Enter the Number: "))
print("Factorial of",num,"=",Factorial(num))

num=int(input("Enter the Number: "))
print("Factorial of",num,"=",Factorial_While(num))