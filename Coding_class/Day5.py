# #Try and Except
a = 1
b = "abc"

try:
    print(a+b)
except TypeError: 
    print("Cannot concatenate")

#multiple error case and else statement
num1 = 100
num2 = "Apple"
num3 = 20 
try:
    c= num1/num3
except (TypeError, ZeroDivisionError, NameError): #we can handle multiple exception errors like this.
    print("Cannot concatenate")
else:
    print(c)
finally:
    print("Finally executed")

class InvalidInputException(Exception): #own error rase concept
    pass
try:
    c = a/b
    raise InvalidInputException("Input is not valid")
except InvalidInputException as e:
    print(c)


##
    
input_a = [1,2,3,4]
input_b = "Mango"
print([a,4])