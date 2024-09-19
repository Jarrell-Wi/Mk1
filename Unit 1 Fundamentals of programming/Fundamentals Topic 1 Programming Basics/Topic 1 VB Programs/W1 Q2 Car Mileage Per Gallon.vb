Module Module1

    Sub main()
        'W1 Q2 Car Mileage Per Gallon

        'declare variable and assign values returned from input boxes

        Dim lastCarMileage As Integer = InputBox("Enter last car milage")
        Dim currentCarmileage As Integer = InputBox("Enter current car milage")
        Dim totalMiles As Integer = currentCarmileage - lastCarMileage
        Dim litresToFillTank As Single = InputBox("Enter litres to fill tank")

        'Declare variables and assign values returned from calculations
        Dim gallonsToFillTank As Single = litresToFillTank / 4.546
        Dim mileage As Single = totalMiles / gallonsToFillTank

        'Concatenate string with variable value using &
        MsgBox("Mileage: " & mileage)

    End Sub

End Module
