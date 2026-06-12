"***This is a Function to Genarate Fibanacci Sequences***"
def WhichFib(n):
    i=0
    j=1
    for k in range(1,n+1):
        i,j=j,i+j
    return i

def WhichFib_While(n):
    i=0
    j=1
    count=0
    while count<n:
        count+=1
        i,j=j,i+j
    return i

num=int(input("Which Fibanacci Number Do You Want: "))
x="Fib({}) = {}"
x=x.format(num,WhichFib(num))
print(x)

num=int(input("Which Fibanacci Number Do You Want: "))
x="Fib({}) = {}"
x=x.format(num,WhichFib_While(num))
print(x)