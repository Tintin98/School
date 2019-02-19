# Program: primeNumbers.py
# Author: Soran Dizay-Loftkaer
# Last date modified: 2/17/19
# Purpose is to find whether and input from the user is prime or not.

prime = input("Please enter a number to see if it is prime:  ")     #Asks for a testable number to see if it is prime

if float(prime) > 1:
    for k in range(2, int(prime)):      #Tests to see if the number is prime
        if (int(prime) % k) == 0:
            print(prime, "is not a prime number.")
            print("Because", prime, "is divided by", k, "it is not possible to be prime")   #Explains why it is not a prime number
            print("A prime number can only be divided by 1 or itself.")
            break
    else:
        print(prime, " is a prime number since it can not be divided evenly by at least 2.")    #Explains why it is a prime number
else:
    print("You need to enter a number larger than 1.")      #Lets the user know of their incorrect input

b = input("Press enter to close the program")