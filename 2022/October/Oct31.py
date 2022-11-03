"""
Problem: Valid Palindrome
Asked by Facebook
Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters.
Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

"""

def validPalindrome(string):
    string = string.lower()
    l,r = 0, len(string)-1
    while (l+r)<len(string) and l>=0 and r>=0:
        if string[l] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            l += 1
            continue
        if string[r] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            r -= 1
            continue
        if string[l] != string[r]:
            return False  
        l += 1
        r -= 1
    return True
print(validPalindrome("A man, a plan,:: a canal: Panama."))