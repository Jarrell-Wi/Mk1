Module Module1


    'W5 Q4 Car Park Subroutines

    Sub Main()

        'AS AQA unit 1 W5 Q4 car park subroutines
        'In this exercise the car parking grid is re-written to use subroutines.

        Dim carPark(9, 5) As String


        emptyCarPark(carPark) 'subroutine call to initialize empty car park
        carPark(0, 0) = "taken" ' set this value to taken for test purposes

        displayParkingGrid(carPark) 'display the grid before parking the car
        parkACar(carPark) ' subroutine call to park the car
        displayParkingGrid(carPark)  'display the grid after parking the car

        MsgBox("End")
    End Sub

    Sub emptyCarPark(ByRef carpark(,) As String)
        For row = 0 To 9
            For column = 0 To 5
                carpark(row, column) = "empty"
            Next
        Next
    End Sub
    Sub parkACar(ByRef carpark(,) As String)
        '--------------------------------------------------------------------------------
        'Now we will attempt to assign a parking space
        'the declared variables below are now "local" to this subroutine.  They do not have "scope" beyond this routine
        Dim emptySpace, rowValid, columnValid As Boolean
        Dim row, column As Integer
        Dim carReg As String = ""

        emptySpace = False
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
            If rowValid And columnValid And carpark(row, column) = "empty" Then
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
        carpark(row, column) = carReg 'if coordinates are valid and space is available then assign space
    End Sub
    Sub displayParkingGrid(ByRef carpark(,) As String)
        Console.Clear() 'clearing the last screen
        'display car park grid
        For row = 0 To 9
            For column = 0 To 5
                Console.Write(carpark(row, column) & vbTab)
            Next
            Console.WriteLine()
        Next
    End Sub
End Module




