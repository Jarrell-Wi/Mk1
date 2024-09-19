#AQA AS PP1 reverse string.py
#reverse the elements of a string
name = input("Please enter name: ")
print(name[0])
name2=[]
length = len(name)
print("length",length)
for n in range(length):
    m = length - n - 1
    print("m",m)    
    name2.append(name[m])
    print(name2)

for n in range(length):
    print(name2[n],end ="")
    
input("\nPress Enter to exit program ")
    

