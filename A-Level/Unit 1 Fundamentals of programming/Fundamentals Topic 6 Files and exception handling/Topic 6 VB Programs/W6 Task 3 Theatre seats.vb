Module Module1
    Sub main()


        'W6 Task 3 Theatre seats

        Dim filename As String = InputBox("Enter a file name to record sales: ")
        Dim performanceDate As String = InputBox("Enter performance date, ddmmyy(xxx to end):")
        Dim validSeatsSold As Boolean = False
        Dim integerSeats As Integer = 0
        Dim seatsSold As String = ""
        Dim fileopened As Boolean = False

        'Open the file to write
        FileOpen(1, filename, OpenMode.Output)

        'While user chooses not to end
        While performanceDate <> "xxx"
            validSeatsSold = False 'Set valid seat to false before checking if true
            While Not validSeatsSold
                seatsSold = InputBox("Enter seats sold:") 'While it is not valid keep trying
                Try
                    integerSeats = Int(seatsSold) 'convert string to integer
                    validSeatsSold = True

                Catch ex As Exception
                    MsgBox("Invalid entry... please re-enter.")
                End Try
            End While
            Write(1, performanceDate) 'write the performance date and seats sold
            Write(1, seatsSold)
            performanceDate = InputBox("Enter performance date, ddmmyy(xxx to end):")
        End While
        FileClose(1) 'close the file

        MsgBox("OK")

        '***************************************************************************
        '********************************** Part 2 of program **********************
        '****************************************************************************

        filename = InputBox("Please enter file name to read seat sales: ")
        MsgBox("Reading audience numbers...")
        Try
            FileOpen(1, filename, OpenMode.Input) 'try to open the file
            fileopened = True 'set the flag to true if successful
        Catch ex As Exception
            MsgBox("File not found... program ending") 'if not successful inform user
            fileopened = False
        End Try
        If fileopened Then 'if fileopened flag is true loop through the file and read data
            While Not EOF(1) 'End Of File (1)
                Input(1, performanceDate) 'input data and write to screen using tab
                Input(1, seatsSold)
                Console.Write("Performance date: " & performanceDate & vbTab & vbTab)
                Console.WriteLine("Seats sold: " & seatsSold)
            End While
        End If

        MsgBox("End of program")
    End Sub

End Module












