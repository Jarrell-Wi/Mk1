ExamScore = int(input('Enter Exam Score: '))
Attendance = int(input('Enter attendance percentage: '))
Scores = [70, 80, 90]
Grades = ['F', 'C', 'B', 'A']
for i in range(len(Scores)):
    if ExamScore >= Scores[i]:
        Grade = i+1
if Attendance > 90:
    print(Grades[Grade])
else:
    print('Get your Attendance up >:(')