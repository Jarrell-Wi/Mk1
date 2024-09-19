Module Module1




    'W5 Q1 Times tables
    Sub Main()
        Dim name As String = ""
        Dim f1 As Integer = 0
        Dim f2s As Integer = 0
        Dim f2e As Integer = 0

        Console.WriteLine("Enter name")
        name = Console.ReadLine
        Console.WriteLine("Enter factor1, factor 2 start and factor 2 end")
        'Get the data for the first factor then the start and end range for the second factor
        f1 = Console.ReadLine()
        f2s = Console.ReadLine()
        f2e = Console.ReadLine()

        'pass values to subroutine call multiples()
        multiples(f1, f2s, f2e, name)

        MsgBox("OK")
    End Sub

    Sub multiples(ByVal factor1 As Integer, ByVal factor2Start As Integer, ByVal factor2End As Integer, ByVal name As String)
        'subroutine takes the factors and displays the times tables

        Console.WriteLine("Hi " & name & " here are your times tables: ")
        Console.WriteLine()
        'Use the start and end range for factor 2 to control the loop

        For i = factor2Start To factor2End
            Console.WriteLine(factor1 & " * " & i & vbTab & " = " & factor1 * i)
        Next

        MsgBox("End")
    End Sub







End Module
