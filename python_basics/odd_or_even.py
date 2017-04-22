# Practice_problems
print("this program tells whether a number you punch in is odd or even\n hit 's' to stop and 'c' to continue")

while True:
    n= input("continue or stop?")
    if n=='c':
        num = int(input('enter any number'))
        if num%2==0:
            print("even")
        else:
            print("odd")
    elif n=='s':
        break
