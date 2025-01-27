# Python Fundamentals

## Data Types
- ```int ``` - any integer
- ```float``` - any decimal
- ```str``` - collect of characters
- ```bool``` - True or False (0 or 1)

## Math operators

**Arithmetic**

- Add ```+```
- Subtract ```-```
- Times ```*```
- Divide ```/```
- Floor divide ```//```
- Modulus (Remainder) ```%```
- Exponent ```*```

**Logical**
- ```and``` - must be both
- ```or``` - at least one must be true
- ```not()``` - opposite
- ```<,>,<=,>=,==,!=``` - inequalties

## String functions

- Use ```[]``` like a list
- Length: ```len()```
- Upper case: ```.upper()```
- Lower case: ```.lower()```
- Replace: ```.replace(*this*,*that*)```
- Split: ```.split(*slicer)```
- Concatenate: ```' '+' '```
- Repeat: ```' '*3```

## Variables

A variable is just a name we can give an objects to make it easier to refer back to it.
For example: <br>```a=3```<br>
```b=1```<br>
```print(a+b)``` <br>
will return ```4```.

## Lists

A list is just a list of objects within ```[]``` seperated by ```,```.<br>
Key functions:
- Initialising: ```x=[ , ]``` or ````x=[f(x) for i in ...]````
- Length: ```len()```
- Slicing: ```x[*start*,*finish*]```
- Changing an entry: ```x[*index*]= ___```
- Add: ```.append(" ")``` ands to end or ```.insert(*index*," ")```
- Remove: ```.remove(" ")```, ```.pop(*index*)``` or ```del x[*index*]```
- Sort: ```.sort()```
- Find index: ```.index(" ")```

## Dictionaries

Dictionaries are just list but instead of having a number index, they have a string (called a key).
They are represented by ```{}``` rather than ```[]```. Key functions:
- Update: ```.update(*Key*," ")```
- Get keys: ```.keys()```
- Get values: ```.values()```
- Add: ```dict[*key*]=" "```
- Remove: ```.pop(*key*)```

## Loops

There are 2 types of loop. If you know how many iterations you need, use ```for```.<br>
For example: ```for i in range(): *do this to i*```<br>
If the number of iterations is unknown or not fixed, use ```while```.<br>
For example: <br>```i=0```<br>
```while i<10: *do this to i*``` **Ensure you change i in the loop or it becomes infinite**

## Functions

A function is a bit of code that we can refer back to that makes it easier to debug and seperate code out. The main look of it is: <br>
```def *FunctionName*:```<br>
```*do this thing*```<br>
```return ___/ print(___)```
