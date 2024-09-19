Module Module1

    Sub Main()
        'W1 Q4 Number of Books
        Dim numberOfBooks As Integer = InputBox("Enter number of books")
        Dim numberOfStudents As Integer = InputBox("Enter number of students")
        Dim numberOfBooksPerStudent As Integer = numberOfBooks / numberOfStudents
        Dim numberLeftOver As Integer = numberOfBooks Mod numberOfStudents


        MsgBox("Number of books per student: " & numberOfBooksPerStudent)
        MsgBox("Books left over: " & numberLeftOver)


    End Sub

End Module
