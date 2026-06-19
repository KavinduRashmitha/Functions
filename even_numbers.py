'''This Function Generates Even Numbers From 1 to N'''
#ForLoop
def EvenNums(n):
    for i in range(2,n+1,2):
        print(i)

#WhileLoop
def EvenNumsWhile(n):
    i=2
    while i<=n:
        print(i)
        i+=2

num=int(input("Enter a Number: "))
EvenNums(num)
print()
EvenNumsWhile(num)