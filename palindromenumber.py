#Given an integer x, return true if x is palindrome integer.
#An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
#This method converts the int to a str first which does use extra space than other methods

class Solution:
    def isPalindrome(self, x: int) -> bool:
        checkvar = str(x)
        if checkvar == str(x)[::-1]:
            return True
        else:
            return False