'''This Function Generates N to 1 Numbers'''
#ForLoop
def NToOne(n):
    for i in range(n,0,-1):
        print(i)

#WhileLoop
def NToOneWhile(n):
    while n>0:
        print(n)
        n-=1

num=int(input("Enter a Number: "))
NToOne(num)
print()
NToOneWhile(num)