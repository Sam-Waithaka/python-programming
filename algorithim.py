#light Algorithim for a palindrome

def is_palindrome(str):
    start_index = 0
    end_index = len(str) -1

    for x in str:
        if str[start_index] != str[end_index]:
            return False
        else:
            return True
        
print(is_palindrome('racecar'))
