Module Module1

    Sub Main()
        'W3 Q3 part numbers

        Dim partnum As String = "xxxx"
        Dim oldModel As Integer = 0
        Dim total As Integer = 0
        Console.WriteLine(partnum & vbTab & oldModel & vbTab & total)

        'Exit condition loop.  The condition is evaluated at the end after the loop has run at least one time
        Do
            Console.WriteLine("Enter part num:")
            partnum = Console.ReadLine
            While Len(partnum) <> 4
                Console.WriteLine("Error enter 4 digit number")
                partnum = Console.ReadLine
            End While
            If Val(partnum(3)) > 5 And Val(partnum(3)) < 9 Then
                oldModel = oldModel + 1
            End If
            total = total + 1
            Console.WriteLine(partnum & vbTab & oldModel & vbTab & total)
        Loop While partnum <> 9999
        Console.WriteLine("Number of old models:" & oldModel)
        MsgBox("OK")


    End Sub

End Module
