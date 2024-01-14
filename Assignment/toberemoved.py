student_marks = {1: 70, 2: 30, 3: 90, 4: 75, 5: 88, 6: 86, 7: 76, 8: 66, 9: 40}

# Set the passing threshold
passing_threshold = 50

# List to store the passing students
passing_students = []

# Iterate through the student marks and check if they have passed the exam
for mark in student_marks.values():
    if mark >= passing_threshold:
        passing_students.append(mark)

# Print the list of passing students
print("List of students who have passed the exam:")
for student in passing_students:
    print(f"Roll: {student}, Mark: {student_marks[student]}")