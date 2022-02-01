#Parameter & Arguments

#Arguments is the value that are sent to the function when it is called.
#Perameter is the variable listed insid the parentheses in the function definition.

#ex>1
def add():    #add just a name,,u can use any name
    a=10
    b=5
    print(a+b)
add()

#ex>2
def add(a,b):
    print(a+b)
add(2,4)

#a,b    >is parameter
#2,4    >is argument

#ex>3
def add(a,b,c):     #its error..cz (a,b,c) is 3..(a+b) is 2 & (2+4) is 2....error
    print(a+b)
add(2,4)