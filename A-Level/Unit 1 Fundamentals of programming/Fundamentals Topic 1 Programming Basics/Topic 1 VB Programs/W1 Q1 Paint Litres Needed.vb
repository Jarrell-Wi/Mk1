Module Module1

    Sub Main()
        'W1 Q1 Paint Litres Needed
        'Declare variables as type integer and then assign the values returned from the input box

        Dim length As Integer = InputBox("Enter length of room")
        Dim width As Integer = InputBox("Enter width of room")
        Dim unusedSpaceLength As Integer = InputBox("Enter lenth of unused space")
        Dim unusedSpaceWidth As Integer = InputBox("Enter width of unused space")
        Dim area As Integer = length * width
        Dim unsuedSpace As Integer = unusedSpaceLength * unusedSpaceWidth
        area = area - unsuedSpace

        'declare the variable and assign the results of the calculation
        Dim litresNeeded = area / 11 'meters squared /Litre

        'Ouptut the string and append the value stored in the variable
        MsgBox("Litres needed: " & litresNeeded)


    End Sub

End Module
