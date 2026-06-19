'''This Function Generates Multiplication Table Which You Want'''
#ForLoop
def MultiplicationTable(n):
    for i in range(1,13):
        print(n,"X",i,"=",n*i)

def MultiplicationTableWhile(n):
    i=1
    while i<13:
        print(n,"X",i,"=",n*i)
        i+=1

num=int(input("Enter the Number: "))
MultiplicationTable(num)
print()
MultiplicationTableWhile(num)