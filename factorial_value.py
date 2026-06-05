"***This is a Function to Find Factorial***"
def Factorial(n):
    tot=1
    for i in range(n,1,-1):
        tot=tot*i
    return tot

num=int(input("Enter the Number: "))
print("Factorial of",num,"=",Factorial(num))