"""
Problem: Reverse String
Asked by Google
Given a string, reverse all of its characters and return the resulting string.

"""

def reverseString(string):
    rstring = ""
    for i in string:
        rstring = i + rstring
    return rstring
print(reverseString("Cat"))