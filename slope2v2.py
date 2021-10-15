#Runway Slope Calculator by Tom Knudsen
#This program takes input from a user and calcualtes the airport's runway slope gradient for use in Boeing 737 FMC
# Version 1.0 - Date 03.07.2019 
# Support and suggestion  post@tknudsen.com

def main(): #Defines a main function
    import time
    import os

    os.system('cls') #Clear Screen
    #Prints out Title Header
    print('///////////////////////')
    print('Runway Slope Calculator')
    print('Version 1.0')
    print('by Tom Knudsen')
    print('///////////////////////')
    print()
    time.sleep(3) #waits for 3 seconds

    #Calculates elevation variance and slope
    elevationH = int(input('Please enter highest runway elevation in feet: ')) 
    time.sleep(1) 
    elevationL = int(input('Please enter lowest runway elevation in feet: ')) 
    time.sleep(1) 
    runwayLenght = int(input('Please enter total runway lenght in meter: ')) 
    time.sleep(1) 
    print('Please wait, calculating....') 
    print() #new line
    time.sleep(2) 
    calculatedElevation = (elevationH - elevationL) 
    calculatedSlope = (calculatedElevation / runwayLenght) * 100  
    
    #Checks and converts the answer into string for concatination and prints out answer appended with string U or string D depending on the value
    if (calculatedSlope) <= 0.0:
        a = (calculatedSlope)
        b = round(a, 1)
        corrected = str(b) + str('D')
        print('Your Runway Slope Gradient is: ', corrected)
    else:
        a = (calculatedSlope)
        b = round(a, 1)
        corrected2 = str(b) + ' ' + str('U')
        print('Your Runway Slope Gradient is: ', corrected2)
    
    time.sleep(1)
    print() #new line
    
    #checks if the user wants to restart the program
    restr=input('Do you want to restart, (y/n): ').lower()
    if restr == 'y':
        print('One second....')
        time.sleep(2)
        main()
    else: 
        print('Have a nice day')
        time.sleep(1)
        exit()

main()