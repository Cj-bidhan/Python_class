#day 5

def add (a,b): #def is function's key word, add is function's name 
    return a + b
c = add(2,3)
d = add("abc","abcd")
try:
    e = add([1,2,3] [1,2,3,4])
except(TypeError, NameError):
    print (c,d,e)
    print("You missed a comma between two lists")
    print("You didnt assign variable a")
     