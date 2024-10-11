#AS AQA unit 1 W2 Q6 Home security system

alarm = "Off"   #initialise alarm
#To test the program, the user must enter information

print("Is the alarm triggered? (Y or N): ", end ="")
trigger = input()
#allow uppcase or lowercase response
trigger = trigger.upper()
if trigger == "Y":
    print("Has movement been detected on ground floor? (Y or N): ",end ="")
    moveGround = input()
    moveGround = moveGround.upper()
    if moveGround == "Y":
        alarm = "On"
        print("Alarm = ",alarm, " Intruder alert ground floor!")
        
    print("Has movement been detected on first floor? (Y or N): ",end ="")
    moveFirst = input()
    moveFirst = moveFirst.upper()

    if moveFirst == "Y":
        alarm = "On"
        print("Alarm = ",alarm, " Intruder alert first floor!")

input("\nPress Enter to exit program ")
    
