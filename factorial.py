def factorial(x):

    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))

num = input("Enter a number\n")
print ("Factorial of " +str(num) + " is "+ str(factorial(num)))