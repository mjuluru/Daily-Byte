"""
Problem: Add Binary
Asked by Apple
Given two binary strings (strings containing only 1s and 0s) return their sum (also as a binary string).
Note: neither binary string will contain leading 0s unless the string itself is 0

"""
def addBinary(num_a, num_b):
    a = integer(num_a, 0)
    b = integer(num_b, 0)
    sum = binary(a+b, "")
    return sum

def integer(num, pos):
    if len(num) == 1:
        return (int(num)*(2**pos))
    return (int(num[-1])*(2**pos)) + integer(num[:-1], pos+1)

def binary(num, final):
    if num == 1 or num == 0:
        return str(num)+final
    remainder = num%2
    quotient = num//2
    return binary(quotient, str(remainder)) + final

print(addBinary("101", "1"))