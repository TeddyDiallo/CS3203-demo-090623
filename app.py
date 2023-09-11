def is_palindrome(string):
"""Return whether (True/False)
    given the string is a palindrome"""

        for i, c in enumerate(string):
            if string[i] != string[len(string)-i-1]:
               return False
        return True


    

