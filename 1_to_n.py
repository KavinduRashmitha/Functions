'''This Function generates 1 To N numbers'''
#ForLoop
def OneToN(n):
    for i in range(1,n+1):
        print(i)

#WhileLoop
def OneToNWhile(n):
    i=1
    while i<=n:
        print(i)
        i+=1

num=int(input("Enter a Number: "))
OneToN(num)
print()
OneToNWhile(num)