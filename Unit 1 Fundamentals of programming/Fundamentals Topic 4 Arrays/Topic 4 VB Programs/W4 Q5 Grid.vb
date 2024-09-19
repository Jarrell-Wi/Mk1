Module Module1


    Sub Main()
        'W4 Q5 Grid
        Dim grid(2, 3) As Char
        Dim rowValue As Integer
        Dim columnValue As Integer

        'initialize grid with value "x"
        For row = 0 To 2
            For column = 0 To 3
                grid(row, column) = "X"
            Next
        Next

        'add "0" top left corner
        grid(0, 0) = "O"
        Console.WriteLine()

        'display grid
        For row = 0 To 2
            For column = 0 To 3
                Console.Write(grid(row, column))
            Next
            Console.WriteLine()
        Next

        'get row and column value for player move
        rowValue = InputBox("Enter row 1 to 3")
        columnValue = InputBox("Enter column 1 to 4")

        'Set grid to "x"
        For row = 0 To 2
            For column = 0 To 3
                grid(row, column) = "X"
            Next
        Next

        'add new location for 0, subtracting one because arrays start at 0
        grid(rowValue - 1, columnValue - 1) = "O"

        Console.WriteLine()

        'display grid with new position
        For row = 0 To 2
            For column = 0 To 3
                Console.Write(grid(row, column))
            Next
            Console.WriteLine()
        Next
        MsgBox("End")

    End Sub




End Module
