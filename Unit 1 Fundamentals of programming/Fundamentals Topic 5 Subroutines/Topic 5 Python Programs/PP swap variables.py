#AQA AS PP5 function to swap two variables
def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b

#********* main program ***********
x = 2
y = 3
print(x,y)
x,y = swap(x,y)
print(x,y)

#the line below will cause the program to crash
#because temp is a local variable in the subroutine
#and is not "in scope" in the main program

print (temp)
