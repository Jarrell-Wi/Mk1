Module Module1

    'W6 Task 1 Maths Workshop
    Sub Main()
        'W6 Q1 write to file
        'program displays menu of options to
        'input, save and print results from maths test

        Dim choice As Integer = displayMenu()
        'create a choice variable and assign the output of display menu

        While choice <> 5 'loop until quit
            'Evaluate the choice and call the appropriate function
            If choice = 1 Then
                saveToFile(2)

            ElseIf choice = 2 Then
                saveToFile(8)

            ElseIf choice = 3 Then
                calculateAverage()

            ElseIf choice = 4 Then
                displayData()

            ElseIf choice = 5 Then
                MsgBox("Quit")
            End If
            'read in new choice
            choice = displayMenu()

        End While

        MsgBox("Close")
    End Sub
    Function displayMenu()
        'this function displays the menu, gets the choice and returns the
        'choice as an integer

        Dim choice As Integer = 0
        Console.WriteLine("1 Input data and save to new file")
        Console.WriteLine("2 Input data and append to existing file")
        Console.WriteLine("3 Calculate and display average mark")
        Console.WriteLine("4 Display Data")
        Console.WriteLine("5 Quit")
        choice = InputBox("Enter choice")

        While choice < 1 Or choice > 5 'choice range check
            choice = InputBox("Invalid data. Enter choice")
        End While

        Return choice

    End Function
    Sub saveToFile(ByVal Mode As Integer)
        'this subroutine takes the mode as an integer 2 = write 8 = append
        'the routine will write a new file or append to an existing one

        Dim studentName As String = ""
        Dim studentMark As Integer = 0
        FileOpen(1, "mathsScores.txt", Mode)
        studentName = InputBox("Enter student name")
        While studentName <> "xxx"
            studentMark = InputBox("Enter mark")
            Write(1, studentName)
            Write(1, studentMark)
            studentName = InputBox("Enter student name")
        End While
        FileClose(1)
    End Sub
    Sub displayData()
        'this subroutine will open the file, read the data and display it

        Dim studentName As String = ""
        Dim studentMark As Integer = 0
        FileOpen(1, "mathsScores.txt", OpenMode.Input)

        While Not EOF(1)
            Input(1, studentName)
            Input(1, studentMark)
            Console.WriteLine("Name: " & studentName & " Mark: " & studentMark)
        End While
        FileClose(1)
    End Sub
    Sub calculateAverage()
        'this routine will open the file read the data, calculate the
        'total and average and write the average to the screen

        Dim studentName As String = ""
        Dim studentMark As Integer = 0
        Dim totalMark As Integer = 0
        Dim count As Integer = 0
        Dim average As Integer = 0
        FileOpen(1, "mathsScores.txt", OpenMode.Input)

        While Not EOF(1)
            Input(1, studentName)
            Input(1, studentMark)
            totalMark = totalMark + Int(studentMark)
            count += 1
        End While
        FileClose(1)
        average = totalMark / count
        Console.WriteLine("Average mark: " & average)
    End Sub
End Module












