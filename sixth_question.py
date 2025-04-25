number = int(input("Enter a number: ")) #This allows the user to enter any integer number
def sum_of_digits(n): #This function takes an integer n as input
    sum = 0
    while n > 0: #As long as n is not equal to zero the while loop continues
        sum += n%10 #inside this loop the last digit of n is extracted using the modulo operator (%10) and added back to s
        n = n//10 #integer division removes the last digit from the number n
    return sum #the calculated sum is then returned
result = sum_of_digits(number)
print(f"The sum of digits of {number} is {result}") #displays the output sum
