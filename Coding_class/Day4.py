#While loop
# num = int (input("Enter a number"))
# i = 1
# while i <= 20:
#     i += 1
#     if i == 10:
#         continue
#     elif i == 15:
#         break      
#     print(f"{num} x {i} = {num * i}")

user_details = []
premission = input (" Do you want to give your details (y/n) ?")
while premission == "y":
    name = input ("Enter: ")
    user_details.append(name)
    premission = input (" Do you want to give your details (y/n) ?")
else:
    print(user_details)
    
    
    
