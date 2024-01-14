# #Asks the user for the number and print the multiplication table of that specific number.
# num1 = int(input("Enter the desigered number: "))
# for i in range (1,21):
#     print (f"{num1} x {i} = {num1}*{i}") 




#You have got the student marks as {1:70, 2:30, 3:90, 4:75, 5:88, 6:86, 7:76, 8:66, 9:40} get the lists of student roll who has pass the exam

passing_threashold = 60 #lets first set the passing threashold
students_marks = {1:70, 2:30, 3:90, 4:75, 5:88, 6:86, 7:76, 8:66, 9:40}#here key is roll number and value is marks
passing_students = [] #created a empty list to stored passed students marks.
for i in students_marks.values():
    if i>=passing_threashold:
        passing_students.append(i) #till this line we have only stored the passed students in the list we created not priented them.
#now to print the list of passed students
print("List of students who have passed the exam: ")
for student in passing_students:
    print (print(f"Roll: {student}, Mark: {students_marks[student]}"))




# #Get the input from user and define the odd and even
# a = int(input("Enter any nummber whose nature you want to find"))
# if a % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")