Module Module1


    Sub Main()
        '    H3 Q2 Password v1 
        Dim attempts As Integer = 1
        Dim password As String = InputBox("Enter password")

        'Loop condition uses And to check two conditions
        While password <> "Tues1212" And attempts < 3

            password = InputBox("Password incorrect - please -renter")
            attempts += 1
        End While

        If password = "Tues1212" Then
            MsgBox("Password accetpted")
        Else
            MsgBox("Password rejected")
        End If
        MsgBox("Press enter to continue")
        End
    End Sub

End Module
