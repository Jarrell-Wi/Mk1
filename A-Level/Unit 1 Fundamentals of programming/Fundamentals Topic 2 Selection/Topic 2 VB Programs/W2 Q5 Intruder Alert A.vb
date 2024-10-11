Module Module1

    Sub Main()
        'W2 Q3 Intruder Alert A
        Dim trigger As Boolean = False
        Dim moveGround As Boolean = False
        Dim moveFirst As Boolean = False
        Dim Alarm As String = "OFF"

        trigger = InputBox("Enter trigger True or False")
        moveGround = InputBox("Enter ground movement sensor True or False")
        moveFirst = InputBox("Enter first floor movement True or False")

        'Using a nested if. If the first condition is true then evaluate the second condition
        If trigger = True Then
            If moveGround = True Then
                Alarm = "ON"
                Console.WriteLine("Intruder alert ground floor!")
                Console.WriteLine("Alarm: " & Alarm)
            ElseIf moveFirst = True Then
                Alarm = "ON"
                Console.WriteLine("Intruder alert first floor!")
                Console.WriteLine("Alarm: " & Alarm)
            End If
        Else
            Console.WriteLine("Family are home")
            Console.WriteLine("Alarm: " & Alarm)
        End If


    End Sub

End Module
