'W3 Q6 Halloween 
Imports System.Threading 'need to import thread.sleep()

Module Module1
    Sub Main()
        Dim light As String = "High"
        Dim pause As Integer = (10 * Rnd()) + 1
        'produces random number 1 to 10

        For i = 1 To 10
            Console.WriteLine(light) 'print the light state
            Console.WriteLine(pause) 'print the pause value
            Thread.Sleep(pause) 'pause 
            'a value of 1000 is one second

            light = "Low"
            pause = Int((10 * Rnd()) + 1) * 100 'assign a new pause interval

            Thread.Sleep(pause) 'thread.sleep() implements pause
        Next
        MsgBox("Press enter to continue")
    End Sub

End Module

