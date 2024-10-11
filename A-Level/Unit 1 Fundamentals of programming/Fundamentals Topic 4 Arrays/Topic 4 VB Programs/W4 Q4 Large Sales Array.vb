Module Module1

    'WS4 Q4 Large Sales Array
    'AS AQA unit 1 W4 Q4 Large Sales array
    Sub Main()
        'Declare arrays and intiliaze with values. 
        Dim numberOfOutlets As Integer = 3 'This will be 50 but I will use 3 for testing
        Dim outletSales(3, numberOfOutlets) As Integer '0 to 3 quarters by number of outlets
        Dim total() As Integer = {0, 0, 0, 0} 'total sales per quarter


        For quarter = 0 To 3
            Console.WriteLine("Quarter " & quarter + 1) 'Output the quarter


            'For each quarter input some data then calculate the total quarter sales quarter
            For outlets = 0 To numberOfOutlets
                outletSales(quarter, outlets) = InputBox("Enter quarter " & quarter + 1 & " for outlet: " & outlets + 1)
                total(quarter) = total(quarter) + outletSales(quarter, outlets)
                Console.WriteLine("Outlet : " & outlets + 1 & "  " & outletSales(quarter, outlets))
            Next
            Console.WriteLine()
        Next


        'Loop throught the total sales and output them to the screen
        For quarter = 0 To 3
            Console.WriteLine("Total per quarter: " & total(quarter))
        Next

        MsgBox("End")
    End Sub




End Module
