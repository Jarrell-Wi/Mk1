Module Module1


    'H5 Q1 Name Arrays
    Sub Main()
        Dim choice As Integer = 0
        Dim names() As String = {"", "", "", "", "", "", "", "", "", ""}
        Do
            choice = displayMenu()
            If choice = 1 Then
                addName(names)
            ElseIf choice = 2 Then
                displayNames(names)
            End If
        Loop While choice <> 3

        Console.WriteLine("Program terminating")

        MsgBox("End")
    End Sub
    Function displayMenu() As Integer
        'This function displays the menu, reads the choice
        Dim choice As Integer = 0
        Console.WriteLine("Choose")
        Console.WriteLine("1 Add Name")
        Console.WriteLine("2 Display list")
        Console.WriteLine("3 Quit")

        While choice < 1 Or choice > 3
            Console.WriteLine("Error choice must be 1 to 3")
            choice = Console.ReadLine
        End While
        Return choice
    End Function

    Sub addName(ByRef names() As String)
        Dim recordNum As Integer = 0
        Console.WriteLine("Enter record number 1 to 10")
        recordNum = Console.ReadLine
        Console.WriteLine("Enter name")
        names(recordNum - 1) = Console.ReadLine

    End Sub

    Sub displayNames(ByVal names() As String)
        For index = 0 To 9
            Console.WriteLine("Record: " & index + 1 & "Name: " & names(index))
        Next

    End Sub

End Module




