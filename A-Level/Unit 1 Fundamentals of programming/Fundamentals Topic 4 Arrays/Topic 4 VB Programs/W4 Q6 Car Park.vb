Module Module1




    Sub Main()

        'W4 Q6 Car Park
        Dim carPark(9, 5) As String
        Dim carReg As String = ""
        Dim row, column As Integer
        Dim emptySpace, rowValid, columnValid As Boolean
        emptySpace = False

        For row = 0 To 9
            For column = 0 To 5
                carPark(row, column) = "empty"
            Next
        Next
        carPark(0, 0) = "taken"

        'display car park grid
        For row = 0 To 9
            For column = 0 To 5
                Console.Write(carPark(row, column) & vbTab)
            Next
            Console.WriteLine()
        Next

        '--------------------------------------------------------------------------------
        'Now we will attempt to assign a parking space

        carReg = InputBox("Enter registration")

        While emptySpace = False


            row = InputBox("Enter row")
            While row < 1 Or row > 10 'Ensure row is a valid range
                row = InputBox("Error enter a number from 1 to 10")
            End While
            row = row - 1 'subtract 1 because the array index starts at 0 and not 1
            rowValid = True 'set the row valid flag to true

            column = InputBox("Enter a column 1 to 6") 'get a valid column number
            While column < 1 Or column > 6
                column = InputBox("Error enter a column from 1 to 6")
            End While
            column = column - 1
            columnValid = True 'set the column valid flag to true
            If rowValid And columnValid And carPark(row, column) = "empty" Then
                emptySpace = True 'set the empty space to true, this space is available
            Else
                'reset the flags to false, re-intialize row and column to 100 and output message
                rowValid = False
                columnValid = False
                row = 100
                column = 100
                MsgBox("That space is taken")
            End If

        End While
        carPark(row, column) = carReg 'if coordinates are valid and space is available then assign space

        'display car park grid
        Console.Clear() 'clearing the last screen
        For row = 0 To 9
            For column = 0 To 5
                Console.Write(carPark(row, column) & vbTab)
            Next
            Console.WriteLine()
        Next

        MsgBox("End")
    End Sub





End Module
