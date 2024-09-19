Module Module1


    Sub Main()
        '    H3 Q2 Password v2 
        Dim attempts As Integer = 1
        Dim password As String = InputBox("Enter password")
        While password <> "Tues1212"
            'This version uses a nested While loop to check two conditions
            While attempts < 3
                password = InputBox("Password incorrect - please -renter")
                attempts += 1
            End While
            If attempts = 3 Then
                Exit While
            End If
        End While
        If password = "Tues1212" Then
            MsgBox("Password accetpted")
        Else
            MsgBox("Password rejected")
        End If

    End Sub


End Module
