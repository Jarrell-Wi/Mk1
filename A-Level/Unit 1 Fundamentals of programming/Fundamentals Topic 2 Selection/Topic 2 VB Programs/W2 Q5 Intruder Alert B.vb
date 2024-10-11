Module Module1

    Sub Main()
        'W2 Q3 Intruder Alert B
        'this is an alternate solution to Alert A where we use Boolean operators rather than nested if statements
        Dim trigger As Boolean = False
        Dim moveGround As Boolean = False
        Dim moveFirst As Boolean = False
        Dim Alarm As String = "OFF"

        trigger = InputBox("Enter trigger True or False")
        moveGround = InputBox("Enter ground movement sensor True or False")
        moveFirst = InputBox("Enter first floor movement True or False")

        If trigger = True And (moveGround = True Or moveFirst = True) Then
            Alarm = "ON"
            Console.WriteLine("Intruder alert!")
        Else
            Console.WriteLine("Family are home")
            Console.WriteLine("Alarm: " & Alarm)

        End If


    End Sub

End Module
