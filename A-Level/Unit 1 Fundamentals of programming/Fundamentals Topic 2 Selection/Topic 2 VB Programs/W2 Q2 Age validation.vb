Module Module1

    Sub Main()
        'W2 Q1 Age validation

        Dim age As Integer = InputBox("Enter your age")

        'check the age range and output the appropriate message
        If age > 10 And age < 19 Then
            Console.WriteLine("Valid age")
        Else
            Console.WriteLine("Invalid input enter a value from 11 to 18")
        End If

        MsgBox("End")


    End Sub

End Module
