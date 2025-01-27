# Python Fundamentals

Python is a widely used language due to the ease for beginners. 
Many of the ideas and functions, especially in the fundamentals and very logical and easy to pick up.
Python is also widely used due to its many libraries and helpful information online.
This means much of the difficult work is already done for you and there are many helpful people out there to solve any problems you come across.

## Data Types
To start, you need to ensure you know the main data types as each of these work differently so it is important to know which one you want to use.
- `int ` - any integer
- `float` - any decimal
- `str` - collect of characters
- `bool` - True or False (0 or 1)

## Math operators
Python has a large collection of libraries which boast different mathematical abilities. 
These can be imported just by using `import` e.g. `import math`. Python also holds many in build functions:

| **Arithmetic**      | **Logical** | **String**                                           |
|---------------------|-----|------------------------------------------------------|
| `+` - add           |`and` - must be both| `*Str*[]` - for location                             |
|  `-` - subtract     |`or` - at least one must be true| `len(*str*)` - length                                |
| `*` - multiply      |`not()` - opposite| `*str*.upper()` - all uppercase                       |
| `/` - divide        |`<,>,<=,>=,==,!=` - inequalties| `*str*.lower()` - all lowercase                      
| `//` - floor divide || `*str*.replace('this','that')` - replace this to that |
| `%` - modulus       ||`*str*.split("Slicer")` - split a sentence to a list of words
| `*` - exponent    ||`' '+' '` or `' '*3` - to concatinate or repeat|


## Variables

A variable is just a name we can give an objects to make it easier to refer back to it.
For example: <br>
```
a=3
b=1
print(a+b)
```
will return `4`.

## Lists

A list is just a list of objects within `[]` seperated by `,`.<br>
Key functions:
- Initialising: `x=[ , ]` or ``x=[f(x) for i in ...]``
- Length: `len()`
- Slicing: `x[*start*:*finish*]`
- Changing an entry: `x[*index*]= ___`
- Add: `.append(" ")` adds to end or `.insert(*index*," ")`
- Remove: `.remove(" ")`, `.pop(*index*)` or `del x[*index*]`
- Sort: `.sort()`
- Find index: `.index(" ")`

## Dictionaries

Dictionaries are just list but instead of having a number index, they have a string (called a key).
They are represented by `{}` rather than `[]`. Key functions:
- Update: `.update(*Key*," ")`
- Get keys: `.keys()`
- Get values: `.values()`
- Add: `dict[*key*]=" "`
- Remove: `.pop(*key*)`

## Loops

There are 2 types of loop. If you know how many iterations you need, use `for`.<br>
For example: 
```
for i in range(): 
    *do this to i*
```
If the number of iterations is unknown or not fixed, use `while`.<br>
For example: 
```
i=0
while i<10: 
    *do this to i*
```
**Ensure you change `i` in the loop or it becomes infinite!**

## Functions

A function is a bit of code that we can refer back to that makes it easier to debug and seperate code out. The main look of it is: <br>
```
def *FunctionName*:
*do this thing*
return ___/ print(___)
```

