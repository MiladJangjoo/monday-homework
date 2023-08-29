# Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors

try:
    age = int(input ("whats your age ?"))
    if age < 18 :
        print ("you are still a baby")
    elif age in range(18,66):
    # elif 18 <= age >= 65: why not working 
        print ("you are grown up")     
    else:
        print("senior")
except:
    print("please enter numeric number")