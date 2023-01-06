# 51: ALIEN AGE
# '0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e', 
# '5': 'f', '6': 'g', '7': 'h', '8': 'i', '9': 'j'
def solution(age):
    answer = ''
    alien_age = {'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e', 
                 '5': 'f', '6': 'g', '7': 'h', '8': 'i', '9': 'j'}
    for i in str(age):
        answer += alien_age[i]
    return answer
    
# 52: MAX MULTIPLY IN LIST
def solution(numbers):
    numbers.sort(reverse = True)
    answer = max(numbers[0] * numbers[1],numbers[-1] * numbers[-2])
    return answer
    
# 53: CALCULATE PIZZA
def solution(n):
    answer = 1
    while (answer*6) % n != 0:
        answer += 1
    return answer
    
# 54: CHANGE CHAR IN STRING
def solution(my_string, num1, num2):
    answer = ''
    my_string = list(my_string)
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    answer = ''.join(my_string)
    return answer
    
# 55: FIND DIGIT'S INDEX IN STRING
def solution(num, k):
    answer = 0
    num = str(num)
    if str(k) in num:
        answer = num.index(str(k))+1
    else:
        answer = -1
    return answer
    
# 55: 369 GAME
def solution(order):
    answer = 0
    game = ['3', '6', '9']
    order = str(order)
    for o in order:
        if o in game:
            answer += 1
    return answer
    
# 56: SORT CHARS IN STRING
def solution(my_string):
    my_string = sorted(my_string.lower())
    answer = ''.join(my_string)
    return answer
    
# 57: REMOVE SAME CHARS
# leave first same char and remove other
def solution(my_string):
    answer = ''
    for s in my_string:
        if s not in answer:
            answer += s
    return answer
    
# 58: FACTORIAL
def solution(n):
    answer = 1
    fac = 1
    while fac <= n:
        answer += 1
        fac = fac * answer
    answer = answer - 1
    return answer
    
# 59: CREATE ONE STRING WITH ANOTHER
# check if one string can be created by other
def solution(before, after):
    answer = 0
    if sorted(before) == sorted(after):
        answer = 1
    else:
        answer = 0
    return answer
    
# 60: MORSE CODE
def solution(letter):
    answer = ''
    morse = {'.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
             '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
             '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
             '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
             '-.--':'y','--..':'z'}
    letter = letter.split(' ')
    for l in letter:
        answer += morse[l]
    return answer
