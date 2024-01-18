#Write a function that uses list comprehensive to generate a list of squares of the numbers from 1 to n
n = int(input("Enter any number"))
def generate_square(number):
    return number**2
def generate_suqare_of_list_of_numbers(*args):#  *args vaneko number of arguments to accept
    print(args)
    for arg in args:
        print(arg)
        print(generate_square(arg))
    return[generate_square(arg) for arg in args]
results = list_of_numbers = range(1, n+1)
value = generate_suqare_of_list_of_numbers(*list_of_numbers)
print(*results)

# generate_suqare_of_list_of_numbers(1,2,3,4,5,6,7)



