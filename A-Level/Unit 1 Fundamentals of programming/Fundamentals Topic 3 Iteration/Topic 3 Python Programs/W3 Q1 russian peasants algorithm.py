#AQA AS Unit 1 Worksheet 3 Question 1
# Russian peasant's algorithm
# This algorithm multiplies two numbers together
print("Enter the first integer: ")
x = int(input())
print("Enter the second integer: ")
y = int(input())
z = 0
print("x =",x, "y=",y,"z=",z, x>0)
while x > 0:
    if x % 2 == 1:
        z = z + y
    #endif
    x = x // 2
    y = y * 2
    print("x =",x, "y=",y,"z=",z, x>0)
#endwhile
print("Product =",z)

input("\nPress ENTER to exit program ")        

