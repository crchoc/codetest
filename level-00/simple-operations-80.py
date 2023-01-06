# 71: SUM OF NUMBERS IN STRING
def solution(my_string):
    answer = 0
    num = ''
    for m in my_string:
        if m.isdigit():
            num += m
        else:
            if len(num) == 0:
                continue
            answer += int(num)
            num = ''
    if len(num) != 0:
        answer += int(num)
    return answer
    
# 72: BALL GAME
# throw ball after one person
def solution(numbers, k):
    answer = numbers[2 * (k-1) % len(numbers)]
    return answer
    
# 73: CHANGE ENGLISH WORDS TO DIGITS
def solution(numbers):
    answer = ''
    ind = 0
    eng = {"zero": '0', "one": '1', "two": '2', 
           "three": '3', "four": '4', "five": '5', 
           "six": '6', "seven": '7', "eight": '8', 
           "nine": '9'}
    for e in eng.keys():
        if e in numbers:
            numbers = numbers.replace(e, eng[e])
    answer = int(numbers)
    return answer
    
# 74: CUT ARRAY INTO PARTS
def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n):
        answer.append(my_str[i:i+n])
    return answer

# 75: Integer factorization
def solution(n):
    answer = []
    fact = []
    i = 2
    while i <= n:
        if n % i == 0:
            fact.append(i)
            n = n // i
        else:
            i += 1
    for i in fact:
        if i not in answer:
            answer.append(i)
    return answer

# 76: CALCULATE STRING FORMULA
def solution(my_string):
    my_string = my_string.split(' ')
    answer = int(my_string[0])
    for i in range(1, len(my_string), 2):
        if my_string[i] == '+':
            answer += int(my_string[i+1])
        else:
            answer -= int(my_string[i+1])
    return answer
