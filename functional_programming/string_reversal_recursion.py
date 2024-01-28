def string_revers(str):
    if len(str) == 0:
        return str
    else:
        return string_revers(str[1:]) + str[0]
    
str = 'reversal'
reverse = string_revers(str)