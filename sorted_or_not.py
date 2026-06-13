"***This is a Function to Check Whether the Given list is Sorted or Not***"
#ForLoop
def IsItSorted(l):
    is_sorted=True
    next=l[0]
    for i in l:
        if i<next:
            is_sorted=False
            break
        else:
            next=i
    return is_sorted


#WhileLoop
def IsItSortedWhile(l):
    is_sorted=True
    before=l[0]
    count=1
    while count<len(l):
        if l[count]<before:
            is_sorted=False
            break
        before=l[count]
        count+=1
    return is_sorted

nums=input("Enter values: ").split(",")
nums=list(map(int,nums))
print(IsItSorted(nums))

nums=input("Enter values: ").split(",")
nums=list(map(int,nums))
print(IsItSortedWhile(nums))