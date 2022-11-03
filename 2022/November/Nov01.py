"""
Problem: Vacuum Cleaner Route
Asked by Amazon
Given a string representing the sequence of moves a robot vacuum makes, 
return whether or not it will return to its original position. 
The string will only contain L, R, U, and D characters, representing left, right, up, and down respectively.

"""

def vacuumCleanerRoute(string):
    horizontal = 0
    vertical = 0
    for i in string:
        if i == "L":
            horizontal += -1
        elif i == "R":
            horizontal += 1
        elif i == "U":
            vertical += -1
        elif i == "D":
            vertical += 1
        
    if horizontal == 0 and vertical == 0:
        return True
    else:
        return False

print(vacuumCleanerRoute("LRUD"))