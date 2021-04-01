import io
import gladysCompute as compute
import gladysSatellite as satellite
import gladysUserLogin as userLogin
"""
   Student:Boi Ngoc Truong
   Module: gladysUserInterface
   Desciption: This module does mmore about using python
"""

def runTests():
    """
        Tests some module function        
    """

    print("running a few tests")

    average = compute .gpsAverage (4, 5)
    print("average = ", average)
        
    print ("hello!")


def start():
    """
        logs the user in, and runs the app
    """

    userName = userLogin.login()
    runApp(userName)


def runApp(userName):
    """
       runs the app
    """
    xCurrPos = -1
    yCurrPos = -1
    xDestPos = -1
    yDestPos = -1
    dist = 0

    # loop until user types q
    userQuit = False
    while (not userQuit):
        # menu
                        
        print('\n-------------------')
        print('Gladys West Map App')
        print('-------------------')
        print('user = ', userName, '\n', sep='')
        print('current position     : x =', xCurrPos, ', y =', yCurrPos)
        print('destination position : x =', xDestPos, ', y =', yDestPos)
        print('distance             :', round(dist, 2), '\n')
        
        print("[c] to set current position")
        print("[d] to set destination position")
        print("[m] to map- which tells the distance")
        print("[t] to run module test")
        print("[q] to quit")

        # get first character of input
        userInput = input("\nEnter a command:")
        lowerInput = userInput.lower()
        firstChar = lowerInput [0:1]

        #menu choices, use a switch-like if-elif control structure
        
        if firstChar == 'c':    # set current position
            xInput = input('Enter a x position:')
            yInput = input('Enter a y position:')
            xCurrPos = int(xInput)
            yCurrPos = int(yInput)
            current = [xCurrPos, yCurrPos]
            destination = [xDestPos, yDestPos]
            dist = compute.distance(current, destination)
        elif firstChar == 'd':  # set destination position
            xInput = input('Enter a x position:')
            yInput = input('Enter a y position:')
            xDestPos = int(xInput)
            yDestPos = int(yInput)
            current = [xCurrPos, yCurrPos]
            destination = [xDestPos, yDestPos]
            dist = compute.distance(current, destination)
        elif firstChar == 'm':    # map - which tells the distance
            print('\n-------------------')
            print('distance = ', dist)
            print('-------------------\n')
        elif firstChar == 'q':    # quit
            userQuit = True
        elif firstChar == 't':    # run some tests (this is part 1 of 2)
            runTests()
        else:
            print("ERROR: " + firstChar + " is not a valid command")

    print("\n")
    print("Thank for using the Gladys West Map App!")
    print("\n")

        
        
