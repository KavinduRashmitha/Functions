'''This Function Calculate Average & Sum of your Marks'''
def Sum(n):
    tot=0
    for i in n:
        tot+=i
    return tot

def Avg(n):
    tot=0
    for i in n:
        tot+=i
    avg=tot/len(n)
    return avg

marks=input("Enter Marks: ").split(",")
marks=list(map(int,marks))
print("Sum =",Sum(marks))
print("Average =",Avg(marks))