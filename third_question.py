number = int(input("Enter a number: ")) #this allows the user to enter an integer that the program will try to find its factorial

def factorial(n):
    if n == 0:
        return 1 #the termination condition
    else:
        return n * factorial(n-1) #the recursive call

print(factorial(number)) #this statement outputs the factorial of the number input by the user.