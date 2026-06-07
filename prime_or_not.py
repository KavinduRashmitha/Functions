"***This is a Function to Check Whether the Given Number is Prime or Not***"
def IsPrime(n):
    is_prime=True
    for i in range(2,n):
        if n%i==0:
            is_prime=False
            break
    return is_prime

num=int(input("Enter the Value: "))
print("Is",num,"Prime :",IsPrime(num))