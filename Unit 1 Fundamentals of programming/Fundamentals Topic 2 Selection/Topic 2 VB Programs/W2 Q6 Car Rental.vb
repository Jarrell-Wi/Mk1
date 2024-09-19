Module Module1

    Sub Main()
        'W2 Q4 Car Rental
        Dim selection As Integer = 0
        Dim selection2 As String = ""
        Console.WriteLine("Enter a choice of:")
        Console.WriteLine("1 Economy Car")
        Console.WriteLine("2 Saloon Car")
        Console.WriteLine("3 Sports Car")
        selection = Console.ReadLine()

        'Use of a Select Case as an alternative to IF..THEN..ELSEIF..
        Select Case selection
            Case 1
                Console.WriteLine("You chose Economy Car")
            Case 2
                Console.WriteLine("You chose Saloon Car")
            Case 3
                Console.WriteLine("You chose Sports Car")
            Case Else
                Console.WriteLine("Invalid choice")
        End Select


        Console.WriteLine("Do you wish to proceed or cancel?")

        selection2 = Console.ReadLine()

        'Using .ToLower converts the answer to lower case to avoid case errors
        If selection2.ToLower = "proceed" Then
            Console.WriteLine("You chose to proceed")
        ElseIf selection2.ToLower = "cancel" Then
            Console.WriteLine("You chose to cancel")
        Else : Console.WriteLine("Invalid entry")
        End If
        Console.WriteLine("Have a nice day")


    End Sub

End Module
