import sys
import time
import threading

def timer():
    m = 0
    s = 0
    timeloop = True
    while timeloop:
        s += 1
        print(str(m) + ' ' +'Minutes ' + str(s) +' ' + 'Seconds')
        time.sleep(1)
        if s == 60:
            s = 0
            m +=1
            print('Minutes:' + str(m))
        elif timeloop == 'q':
            break

    

print("This is a timer (Press 'q' if you want to stop the timer).")
def asking():
    while True:
        ask = input("Would you like to start the timer (yes/no): ")

        if 'y' in ask:
            print("Press 'G' to start timer(Press s to stop/g to go)")
            timeloop = True
            timer()
            break
        elif 'n' in ask:
            print("Ok not going to start the timer")
            quit = input("Do you want to quit(yes/no): ")

            if 'n' in quit:
                print("Okay")
                asking()
            elif 'y' in quit:
                print("Okay quitting now")
                sys.exit()
        else:
                print("Sorry that was not an answer")
                asking()

asking()
