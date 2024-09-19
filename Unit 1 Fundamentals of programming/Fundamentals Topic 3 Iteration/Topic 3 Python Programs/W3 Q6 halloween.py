import time
import random
# the next statement would cause the loop to continue indefinitely
#... very inconvenient,so we'll substitute a FOR ..ENDFOR loop
# while True:
for counter in range (10):
    light = "high"
    print(light)
    x=random.randint(1,10)/100
    print(x)
#time.sleep(5) waits for 5 seconds
    time.sleep(x)  #pause for a few seconds
    light = "low"
    print(light)
    x=random.randint(1,10)/100
    print(x)      
    time.sleep(x)
