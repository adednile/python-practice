def check_even_or_odd(num):
    try:  #Ideally the user would be able to enter a number, any number even a float but this check that the number entered is an integer and if not outputs an error
        num = int(num)
        if num % 2 == 0:
            print(f'{num} is even')
        else:
            print(f'{num} is odd')
    except ValueError:
        return "Invalid entry, please enter an integer"
input_number = input("Enter an integer: ") #prompts the user to enter an integer
result = check_even_or_odd(input_number) #passes the number entered by the user to the check function
print(result) #outputs the conclusive proof










#num = input('Enter a number: ')
#if num % 2 == 0:
 #   print(f'{num} is even')
#else:
 #   print(f'{num} is odd')
#   TypeError: not all arguments converted during string formatting