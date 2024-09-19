Module Module1



    Sub Main()
        'PP6 binary graphic file and copy it to another file

        Dim file As String = "U:\waterlilies.jpg"
        Dim file2 As String = "U:\waterlilies2.jpg"
        Dim buffer As Integer = 50000

        'set a buffer size so memory does not overflow
        'the graphic is 476KB

        Dim tempFile = IO.File.Open(file, IO.FileMode.Open)

        ' Adjust array length for VB array declaration. 
        Dim bytes = New Byte(buffer - 1) {}

        While tempFile.Read(bytes, 0, buffer) > 0
            My.Computer.FileSystem.WriteAllBytes(file2, bytes, True)
            Console.Write(".")
        End While

        tempFile.Close()


        MsgBox("OK")

    End Sub





End Module




