#for loop
fruits = ["apple", "mango", "Bananna", "Orange"]
for fruit in fruits:
     print(fruit)

###

[print(fruit) for fruit in fruits] #list comperhensive method. (same output as above code)

###
for fruit in fruits:
    if fruit == "Orange":
     print("Will break the program")
    break #this line will break the loop sequence
#     print(fruit)

for fruit in fruits:
    if fruit =="Orange":
        print("Will break the program")
        continue #this line will not exictue the code below this line but will start over again
        print("Will not be exicuted")
    print(fruit)
