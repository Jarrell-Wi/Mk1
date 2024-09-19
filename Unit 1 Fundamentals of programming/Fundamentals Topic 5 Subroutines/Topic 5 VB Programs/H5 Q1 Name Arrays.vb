Module Module1


    Sub Main()

        'AQA AS PP L6 write to and read from car file
        'program to append data to a text file
        'if the file does not exist, it will be created 

        Dim file As String = "carFile.txt"
        Dim carModel As String = ""
        Dim carPrice As Integer = 0
        Dim totalCarPrice As Integer = 0
        Dim wholeCarFile As String = ""
        Dim carFileLine As String = ""
        Dim x(1) As String
        Dim y As String = ""

        'Open the file. File number 1. Pass the file name and set the mode to append
        FileOpen(1, file, OpenMode.Append)
        Console.WriteLine("This program lets you enter records to a file called carFile.txt")
        Console.WriteLine("If the file doesn't exist, it will be created.")

        'get the data and terminate by typing in xxx
        carModel = InputBox("Enter car model:")
        While carModel <> "xxx"
            carPrice = InputBox("Enter price of car:")

            'writeline is similar to console.writeline("xxx") without the console and it takes a file number
            WriteLine(1, carModel & "," & carPrice)
            carModel = InputBox("Enter car model")
        End While
        FileClose(1) 'Close the file
        Console.WriteLine("The file has been closed and reopened for reading")

        'Open the file with mode set to input
        FileOpen(1, file, OpenMode.Input)

        'While it is not the end of file EOF(1) use Input(1,variable) to read the data
        While Not EOF(1)
            Input(1, carFileLine)
            wholeCarFile = wholeCarFile & carFileLine ' concatenate data into a single string
        End While
        FileClose(1) 'close the file

        Console.WriteLine("Whole file: " & wholeCarFile) 'output file contents

        FileOpen(1, file, OpenMode.Input) ' Open the file
        While Not EOF(1)
            Input(1, carFileLine)

            x = carFileLine.Split(",")
            totalCarPrice = totalCarPrice + x(1)
            Console.WriteLine("Total price: " & totalCarPrice)
        End While

        FileClose(1)

        MsgBox("OK")
    End Sub


End Module




