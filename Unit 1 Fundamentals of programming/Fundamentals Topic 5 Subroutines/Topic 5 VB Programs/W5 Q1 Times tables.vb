Module Module1



    Sub main()


        'W5 Q2 return multiple values
        '# pass multiple results back from a function
        'In python it is possible to return multiple values from a function
        'in other languages such as VB it is only possible to return one value from a function
        'to return multiple values it would be necessary to pass them as parameters by reference
        'you would then be able to change the value of variable outside the subroutine

        Dim add, subtract, multiply As Integer

        calc(add, subtract, multiply, 5, 3)
        Console.WriteLine(add)
        Console.WriteLine(subtract)
        Console.WriteLine(multiply)

        MsgBox("End")
    End Sub
    Sub calc(ByRef a As Integer, ByRef s As Integer, ByRef m As Integer, ByVal x As Integer, ByVal y As Integer)
        a = x + y
        s = x - y
        m = x * y
    End Sub

End Module
