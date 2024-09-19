Module Module1


    Sub Main()
        'W4 Q1 Reverse Order
        Dim total As Integer = 0
        Dim numbers(5) As Integer
        Dim average As Integer = 0

        'add values to the array
        For index = 0 To 5
            numbers(index) = InputBox("Enter a number")
            total = numbers(index) + total
        Next

        'output values while stepping down from 5 to 0
        For index = 5 To 0 Step -1
            Console.WriteLine("Number" & index & " is: " & numbers(index))
        Next
        average = total / 6

        Console.WriteLine("The total is : " & total)
        Console.WriteLine("The average is : " & average)


    End Sub


End Module
