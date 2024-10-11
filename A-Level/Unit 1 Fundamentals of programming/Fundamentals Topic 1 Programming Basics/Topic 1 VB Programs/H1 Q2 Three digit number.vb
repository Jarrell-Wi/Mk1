Module Module1

    Sub Main()
        'H1 Q2 Three digit number hundreds, tens and units

        Dim threeDigitNumber As Integer = InputBox("Enter a two digit number")
        'NOTE vb forward slash / = normal division back slash \ = integer division
        'Remember that Mod returns the remainder

        Dim hundreds As Integer = threeDigitNumber \ 100
        Dim tens As Integer = (threeDigitNumber Mod 100) \ 10
        Dim units As Integer = (threeDigitNumber Mod 100) Mod 10
        MsgBox(hundreds)
        MsgBox(tens)
        MsgBox(units)


    End Sub

End Module
