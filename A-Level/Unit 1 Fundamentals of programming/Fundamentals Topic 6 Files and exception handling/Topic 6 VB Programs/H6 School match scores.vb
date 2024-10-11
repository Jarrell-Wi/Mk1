Module Module1
    Dim maxArray As Integer = 2 'global variable allows you to easily change array size for testing
    Sub Main()
        'H6 School match scores

        Dim schools(maxArray) As String
        Dim wins(maxArray) As Integer
        Dim filename As String = "U:\teamScores.txt"
        Dim choice As Integer = menu()
        While choice <> 6
            Select Case choice
                Case 1
                    load(schools, wins, filename)
                Case 2
                    getData(schools, wins)
                Case 3
                    save(schools, wins, filename)
                Case 4
                    displayData(schools, wins)
                Case 5
                    menu()
                Case 6
                    Console.WriteLine("You have chosen to the end the program")
            End Select
            choice = menu()

        End While

    End Sub
    Sub load(ByRef schools() As String, ByRef wins() As Integer, ByVal filename As String)
        FileOpen(1, filename, OpenMode.Input)
        For index = 0 To maxArray
            Input(1, schools(index))
            Input(1, wins(index))
        Next
        FileClose(1)
        MsgBox("File read")
    End Sub
    Sub save(ByVal schools() As String, ByVal wins() As Integer, ByVal filename As String)
        FileOpen(1, filename, OpenMode.Output)
        For index = 0 To maxArray
            Write(1, schools(index))
            Write(1, wins(index))
        Next
        FileClose(1)
        MsgBox("File written")
    End Sub
    Sub displayData(ByVal schools() As String, ByVal wins() As Integer)
        For index = 0 To maxArray
            Console.WriteLine("School: " & schools(index) & vbTab & " Number of wins: " & vbTab & wins(index))
        Next
    End Sub
    Sub getData(ByRef schools() As String, ByRef wins() As Integer)
        Dim valid As Boolean = False
        For index = 0 To maxArray
            schools(index) = InputBox("Enter school name: ")
            valid = False
            While valid = False
                Try
                    wins(index) = InputBox("Enter wins 0 to 20")
                    While wins(index) < 0 Or wins(index) > 20
                        wins(index) = InputBox("Error. Enter wins 0 to 20")
                    End While
                    valid = True

                Catch ex As Exception
                    MsgBox("Error. Enter an integer")
                End Try
            End While
        Next
    End Sub
    Function menu() As Integer
        Dim response As Integer

        Console.WriteLine("Select from the following:")
        Console.WriteLine("1 Load data")
        Console.WriteLine("2 Enter new data")
        Console.WriteLine("3 Save data")
        Console.WriteLine("4 Display data")
        Console.WriteLine("5 Menu options")
        Console.WriteLine("6 Quit")

        response = Console.ReadLine

        While response < 1 Or response > 6
            Console.WriteLine("Error enter number 1 to 6")
            response = Console.ReadLine
        End While
        Return response
    End Function

End Module













