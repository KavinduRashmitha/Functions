'''This Function Generates Even Numbers from 1 to N'''
#ForLoop
def OddNums(n):
    for i in range(1,n+1,2):
        print(i)

#WhileLoop
def OddNumsWhile(n):
    i=1
    while i<=n:
        print(i)
        i+=2

num=int(input("Enter a Number: "))
OddNums(num)
print()
OddNumsWhile(num)