"***This is a Function to Check Whether the Given Number is Prime or Not***"
def IsPrime(n):
    is_prime=True
    for i in range(2,n):
        if n%i==0:
            is_prime=False
            break
    return is_prime

def IsPrimeWhile(n):
    is_prime=True
    count=2
    while count<n:
        if n%count==0:
            is_prime=False
            break
        count+=1
    return is_prime

num=int(input("Enter the Value: "))
print("Is",num,"Prime :",IsPrime(num))

num=int(input("Enter the Value: "))
print("Is",num,"Prime :",IsPrimeWhile(num))