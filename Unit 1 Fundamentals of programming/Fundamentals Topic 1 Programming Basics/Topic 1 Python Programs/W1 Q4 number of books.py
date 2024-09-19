#AQA AS W1 Q4 Number of Books
numberOfStudents = int(input("Enter number of students: "))
numberOfBooks = int(input("Enter number of books: "))
booksPerStudent = numberOfBooks // numberOfStudents
leftOver = numberOfBooks % numberOfStudents
print("Books per student: ",booksPerStudent)
print("Books left over: ", leftOver)
