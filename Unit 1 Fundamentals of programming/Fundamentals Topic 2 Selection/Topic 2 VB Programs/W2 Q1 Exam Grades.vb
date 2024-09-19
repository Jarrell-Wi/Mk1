Module Module1

    'W2 Q2 Exam Grades


    Sub Main()
        Dim mark As Integer = InputBox("Enter exam mark")
        Dim attendance As Integer = InputBox("Enter attendance")

        'Check multiple ranges and return the appropriate response
        If attendance > 90 Then
            If mark > 90 And mark < 101 Then
                Console.WriteLine("Grade A")
            ElseIf mark > 80 And mark <= 90 Then
                Console.WriteLine("Grade B")
            ElseIf mark > 70 And mark <= 80 Then
                Console.WriteLine("GradeC")
            Else
                Console.WriteLine("Fail")
            End If
        Else
            Console.WriteLine("Fail")
        End If

        MsgBox("End")
    End Sub


End Module
