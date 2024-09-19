Module Module1

    Sub Main()
        'H2 Q2 Temperature and Humidity
        Dim temp As Integer = 0
        Dim humidity As Integer = 0

        Console.WriteLine("Enter the temperature")
        temp = Console.ReadLine

        Console.WriteLine("Enter the humidity")
        humidity = Console.ReadLine

        If temp > 25 Or humidity < 50 Then
            Console.WriteLine("Open the window")
        Else
            Console.WriteLine("Close the window")
        End If


    End Sub

End Module
