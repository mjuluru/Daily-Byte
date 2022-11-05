"""
Problem Longest Common Prefix
Asked by Microsoft
Given an array of strings, return the longest common prefix that is shared amongst all strings.
Note: you may assume all strings only contain lowercase alphabetical characters.

"""

def longestCommonPrefix(arr):
    common = arr[0]
    for i in range(1,len(arr)):
        if common in arr[i]:
            continue
        else:
            while True:
                common = common[:-1]
                if common == str(arr[i])[0:len(common)]:
                    break
    return common

print(longestCommonPrefix(["a", "b", "c"]))