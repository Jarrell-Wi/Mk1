Module Module1




    'PP Try Except Example 3
    Sub Main()
        Dim ageValid As Boolean = False
        Dim age As Integer = 0
        While age < 11 Or age > 18
            Try
                age = InputBox("Enter age")
            Catch ex As Exception

                age = InputBox("Please enter an integer")
            End Try
        End While
        Console.WriteLine("You entered an age of " & age)
        MsgBox("OK")
    End Sub






End Module




