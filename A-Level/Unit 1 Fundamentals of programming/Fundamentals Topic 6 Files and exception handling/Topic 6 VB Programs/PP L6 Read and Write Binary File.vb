Module Module1




    'PP L6 Read and Write Binary Files 100 Numbers

    Sub Main()
        'process a binary file
        'write 100 integers to a file
        'read them again and add them up

        'read into a separate array to demonstrate that the 
        'array contents comes from the file and are not generated in the code

        Dim filename As String = "numbers.bin"
        Dim number(99) As Integer
        Dim number2(99) As Integer
        Dim sum As Integer = 0

        For i = 0 To 99
            number(i) = i
        Next
        FileOpen(1, filename, OpenMode.Binary, OpenAccess.Write)
        FilePut(1, number)
        FileClose()
        MsgBox("Binary file written")

        FileOpen(1, filename, OpenMode.Binary, OpenAccess.Read)
        FileGet(1, number2)
        FileClose(1)
        MsgBox("Binary file read")

        'Optional section of code to print the values to view 
        'the contents of the file. Stepped in values of 2 using a tab to align
        'the data in columns to make it easier to read.

        For i = 0 To 99 Step 2
            Console.Write(i)
            Console.Write(vbTab)
            Console.Write(i + 1)
            Console.WriteLine()
        Next
        'this loop sums the data in the array read from the file.
        For i = 0 To 99
            sum = sum + number2(i)
        Next
        MsgBox("The sum is : " & sum)
        MsgBox("OK")
    End Sub





End Module




