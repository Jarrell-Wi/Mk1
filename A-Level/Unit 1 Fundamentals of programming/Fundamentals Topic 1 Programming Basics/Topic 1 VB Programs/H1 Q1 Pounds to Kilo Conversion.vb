Module Module1

    Sub Main()

        'H1 Q1 Pounds to Kilo Conversion

        Dim kiloValue As Single = InputBox("Enter kilo value to convert")
        Dim poundValue As Single = InputBox("Enter pound value to convert")

        'one method of conversion
        Dim kiloToPounds As Single = kiloValue * 2.20462
        Dim poundsToKilos As Single = poundValue * 0.453592

        'this is an equally valid method of conversion
        Dim kToPmethod2 As Single = kiloValue / 0.453592
        Dim pToKmethod2 As Single = poundValue / 2.20462

        MsgBox("Kilo to pounds " & kiloToPounds)
        MsgBox("Pounds to kilos " & poundsToKilos)
        MsgBox("Kilo to pounds " & kToPmethod2)
        MsgBox("Pounds to kilos " & pToKmethod2)

    End Sub

End Module
