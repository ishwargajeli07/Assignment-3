#Taking a Number input from user
num = int(input("Enter a Number: "))

#Calculating Factorial using Recursion
def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num * fact(num-1)
#Printing the Output
print("The factorial of the number", num ,'is', fact(num))
