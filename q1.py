"""

# -----------------------
# File      : q1.py
# Created   : 30/09/21 2:07 PM
# Author    : Ron Greego
# Version   : v1.0.0
# Description : Test loop with pass, break and continue
# --------------------------
"""

if __name__ == '__main__':
    i = 0
    while 1:
        print("Inside the while loop")
        if i == 5:
            print("Condition satisfied ! Exiting from the loop")
            break
        else:
            print("Inside else condition")
            i += 1

        print("Continue iteration")

    print("Outside the while loop")