#process a binary file
#write 100 integers to a file
#then read them back and add them up


#data is encoded into binary format with the struct.pack() function
#and decoded with the struct.unpack()function
#The built-in struct module has to be imported
import struct

#open the file for writing in binary mode, indicated by "wb"
fileOfIntegers = open("binaryfile.dat","wb")
print("Binary file opened for writing")


# the statement num = struct.pack('i',n)
#tells Python that num is an integer, denoted by parameter "i" for "integer"
for n in range (100):
    num = struct.pack('i',n)
    fileOfIntegers.write(num)
fileOfIntegers.close
print("Binary file closed")

#now read the file of numbers and calculate the sum of the integers
total = 0
fileOfIntegers = open("binaryfile.dat","rb")
print("Binary file opened for reading")
#calculate the size of an integer
integerSize = struct.calcsize("i")
print ("\nSize of an integer = ",integerSize,"\n")

#read the data in the file i bytes at a time until all data is read
bytesRead = fileOfIntegers.read(integerSize)
while bytesRead:
    num = struct.unpack("i",bytesRead)

#convert from a list to a simple variable
    num = num[0]
    total = total + num
    print(num, end = " ")
    bytesRead = fileOfIntegers.read(integerSize)
fileOfIntegers.close()
print("\n\nBinary file closed")
print("\nTotal = ",total)


