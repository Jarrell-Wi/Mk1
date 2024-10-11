Module Module1

    Sub Main()
        'W3 Q2 fever
        Dim temp As Single = 0
        Dim Hour As Integer = 1
        Dim total = 0
        Dim average = 0
        Dim fever = 0
        Console.WriteLine(temp & vbTab & Hour & vbTab & fever & vbTab & total & vbTab)

        'entry condition loop - while Hour < 7
        While Hour < 7
            Console.WriteLine("Enter temp")
            temp = Console.ReadLine()
            If temp > 37 Then
                fever = fever + 1
            End If
            total = total + temp
            Hour = Hour + 1 'Hour is incremented inside loop, if not then we would have an infinite loop

            Console.WriteLine(temp & vbTab & Hour & vbTab & fever & vbTab & total & vbTab)
        End While
        average = total / Hour
        Console.WriteLine(Hour & vbTab & total & vbTab & average)
        Console.WriteLine("Fever reading: " & fever)


    End Sub

End Module
