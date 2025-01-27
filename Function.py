
import math as m


print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:

def listprime(a):
    y=[]
    for i in range(1,a+1):
        if a%i==0:y.append(i)
    return y


print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:

def factor(a,b):
    if b>a:
        a,b=b,a
    if a%b==0: return True
    else: return False



# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:

def letter(a):
    a.lower()
    return alphabet.index(a)



print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:

def codename(name):
    code=""
    for i in name.lower():
        code=code+str(letter(i))
    return code


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:

def passwords(a):
    code=codename(a)
    minus=0
    for i in code:
        minus+=int(i)
    return int(code)-minus


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:

def isprime(a):
    b = m.ceil(m.sqrt(a)) + 1
    factor = 0
    for i in range(2, b):
        if a % i == 0: factor = factor + 1
    if a == 0 or a == 1:
        return False
    elif factor == 0 or a == 2:
        return True
    else:
        return False

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:

def isprime(a):
    if type(a)!=int:
        a=int(a)
    b = m.ceil(m.sqrt(a)) + 1
    factor = 0
    for i in range(2, b):
        if a % i == 0: factor = factor + 1
    if a == 0 or a == 1:
        return False
    elif factor == 0 or a == 2:
        return True
    else:
        return False


# -------------------------------------------------------------------------------------- #






