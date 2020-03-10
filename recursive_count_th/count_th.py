'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
my_string = 'qwththgthklh'

def count_th(word):
    count = 0
    if word == 'th':
        return 1
    if len(word) <= 2 and not word == 'th':
        return 0
    else:
        break_point = len(word)//2
        first_half = word[:break_point]
        second_half = word[break_point:]
        count = count_th(first_half) + count_th(second_half)
        fw = word[len(word)//2 - 1]   
        sw = word[len(word)//2]  
        return count + count_th(fw + sw)  
        
print(count_th(my_string))    