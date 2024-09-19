Module Module1



    'W4 Q3  Sales Array

    Sub Main()
        'Declare arrays and intiliaze with values. 
        Dim outlet1Sales() As Integer = {10, 12, 15, 10}
        Dim outlet2Sales() As Integer = {5, 8, 3, 6}
        Dim outlet3Sales() As Integer = {10, 12, 15, 10}
        Dim total() As Integer = {0, 0, 0, 0}

        'Loop through array and total sales data for each quarter then output data to screen
        For quarter = 0 To 3
            total(quarter) = total(quarter) + outlet1Sales(quarter) + outlet2Sales(quarter) + outlet3Sales(quarter)
            Console.WriteLine("Total for quarter : " & quarter + 1 & vbTab & total(quarter))
        Next
        MsgBox("End")


    End Sub


End Module
