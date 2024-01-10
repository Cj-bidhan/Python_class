#To daiplay string, consider 'a' to be string
a = "Hello World"
b = """This is second string, This is a third string, a, b""" #Triple quotes can be used to display multiple strings
print (a) 
print (b)


#String indexing, length, check if, check if not
print(a[1]) #Get the character at position 1 
print(b[2]) #Get the character at position 2 
print(len(a)) #To get the length of sting a.
txt = "This ia a selfish world that we live in!!!"
print("selfish" in txt) #To check if a certain phrase or character is present in a string
print("Selfless" in txt)
print("Slefless" not in txt) ##To check if a certain phrase or character is not present in a string

#To display list,
numlist = [1,2,3,4,5]
print(numlist)
strlist = ["apple", "bananna", "cherry", "pine"]
print(strlist)
mixlist =[1, 2, "apple", True, 34]
print(mixlist)
lista = [1,2,1,0, [a,b],{1,2,3}]
newlist = list(numlist + strlist)
print(newlist)

#We also have list constructor
constructlist = list(("apple","bananna",1,2,3,4,))
print(constructlist)

#To display Tuple
firsttuple = ("apple", "Bananna", "Momo")
print(firsttuple)

#We also have tuple constructor
pretuple = tuple(("apple", "Bananna", "Momo"))
print(pretuple)

#To display sets
aset = {1,2,"apple", True, 0 , False }
print(aset)
bset = set((1,2,'apple'))
print(bset)

##Mathematical calculations
a= int(input ("Enter first number"))
b= int(input ("Enter second number"))
add = a + b
sub = a - b
multi = a * b
divide = a / b
remaindar = a // b
print("Addition of two number is: " + str(add ))
print("Subtraction of two number is: " +str(sub) )
print("Multiplication of two number is: " +str(multi))
print("Division of two number is: " + str(divide))
print ("Remainder of two number is: " +str(remaindar))
print ("Hello World")

