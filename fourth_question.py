#creating the reverse string function
def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char +reversed_s
    return reversed_s

my_string = input("Enter a string: ") #this will prompt the user to enter any set of characters
reversed_string = reverse_string(my_string) #this passes the user's input to the function for reversal
print(reversed_string) #This displays the reversed string as output