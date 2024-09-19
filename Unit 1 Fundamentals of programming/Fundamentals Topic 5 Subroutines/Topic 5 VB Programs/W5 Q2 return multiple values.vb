Module Module1




    Sub Main()
        'W5 Q3 password
        'Ask the user to type in a password twice and verify it is the same
        'declare variables to hold both attempts and get value by passing the returned value
        'from the function getPword.  Pass a value 1 or 2 to determine if it is the first or second attempt

        Dim pword1 As String = getPword(1)
        Dim pword2 As String = getPword(2)

        'While the passwords are not the same inform user and prompt to re-enter passwords
        While pword1 <> pword2
            Console.WriteLine("Error passwords do not match")
            pword1 = getPword(1)
            pword2 = getPword(2)
        End While

        Console.WriteLine("Password change successful")

        MsgBox("OK")
    End Sub
    Function getPword(ByVal attempt As Integer) As String
        Dim pword As String = ""
        If attempt = 1 Then
            Console.WriteLine("Enter your password")
        ElseIf attempt = 2 Then
            Console.WriteLine("Enter your password again")
        End If

        pword = Console.ReadLine
        While Len(pword) < 5 Or Len(pword) > 8
            Console.WriteLine("Error. Password must be 6 to 8 characters long.")
            pword = Console.ReadLine

        End While
        Return pword

    End Function




End Module
