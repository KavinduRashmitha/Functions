"***This is a Function to Check if the Target Number Available in the given List***"
def IsItIn(l,n):
    is_it_available=False
    if n in l:
        is_it_available=True
    return is_it_available

nums=input("Enter Values: ").split(",")
n=int(input("Target Number: "))
nums=list(map(int,nums))
print(IsItIn(nums,n))