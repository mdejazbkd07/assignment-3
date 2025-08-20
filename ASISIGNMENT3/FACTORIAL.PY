def fact():
    factorial=1
    for i in range (1,n+1):
        factorial=factorial*i
    return factorial

n=int(input("enter a number : "))
print(f"Factorial of {n} is : {fact()}")