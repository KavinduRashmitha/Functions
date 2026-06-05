"***This is a Function to Genarate Fibanacci Sequences***"
def WhichFib(n):
    i=0
    j=1
    for k in range(1,n+1):
        i,j=j,i+j
    return i

num=int(input("Which Fibanacci Number Do You Want: "))
x="Fib({}) = {}"
x=x.format(num,WhichFib(num))
print(x)