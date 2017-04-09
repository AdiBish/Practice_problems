# checking whether a number is prime or not :
while True:
    n= input("hit 'c' to continue or 's' to stop")
    if n =='c':
        n=int(input("enter numbetr"))
        for i in range (2,n):
            if n%i == 0:
                print (n, " is not prime")
                break
            else:
                print(n, "is prime")
                break 
    elif n == 's':
        break
