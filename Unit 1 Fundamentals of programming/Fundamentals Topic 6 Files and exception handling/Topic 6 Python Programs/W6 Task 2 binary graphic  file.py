#PP L6 binary graphic file
#and copy it to another file

#set a buffer size so memory does not overflow
#the graphic is 476KB
buffersize = 50000
picturefile = open('waterlilies.jpg','rb')
print('File opened')
newfilename = input("Enter the new file name to copy image to: ")
copiedfile = open(newfilename,'wb')

#read 50000 bytes at a time
buffer = picturefile.read(buffersize)
#print a dot every time 50K bytes are written
while len(buffer):
   copiedfile.write(buffer)
   print('.', end = '')
   buffer = picturefile.read(buffersize)
print()
print('file copied ... look in folder!')


              
