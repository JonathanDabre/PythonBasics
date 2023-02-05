import time

hour = int(time.strftime('%H'))

if(16 > hour > 12):    
    print("Good Afternoon!")
elif(hour > 16):
    print("Good Evening!")    
elif(5 > hour > 0):
    print("Ohh! its midnight. No sleep?")
else:
    print("Good Morning!!")   
