"""
Problem: Correct Capitalization
Asked by Google
Given a string, return whether or not it uses capitalization correctly. 
A string correctly uses capitalization if all letters are capitalized, 
no letters are capitalized, or only the first letter is capitalized.

"""

def correctCapitalization(string):
    for i in range(len(string)):
        if i == 0:
            if string[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                continue
            else:
                break
        if string[i] in "abcdefghijklmnopqrstuvwxyz":
            continue
        else:
            break
    if i == (len(string)-1):
        return True
    else:
        return False
print(correctCapitalization("POITUHJ"))