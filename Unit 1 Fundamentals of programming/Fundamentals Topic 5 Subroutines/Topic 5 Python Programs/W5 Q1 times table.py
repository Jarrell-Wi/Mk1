#AS AQA unit 1 W5 Q1 Times tables
def multiples(f1,f2start,f2end,name):
	print("Hi,",name,  "... here is your times table")
	for index in range (f2start, f2end+1):
		print (f1, " x ", index, " = ", f1 * index)
	#END FOR
#ENDSUB

#main program
print ("What is your name? ") 
name = input()
print ("Enter times table, start number and end number ")
table = int(input())
startnum = int(input())
endnum = int(input())
multiples(table,startnum,endnum,name)
