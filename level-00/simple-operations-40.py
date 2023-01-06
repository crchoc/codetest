# 31: ODD nums in REVERSE ORDER
# n 이하의 홀수가 오름차순으로 담긴 배열을 return
def odds_in_reverse(n):
    answer = []
    for i in range(n, 0, -1):
        if i % 2 != 0:
            answer.append(i)
    answer.reverse()
    return answer
  
  
# 32: CALCULATE SAME CHARS IN TWO STRINGS
def same_chars(s1, s2):
    answer = 0
    for one in s1:
        for two in s2:
            if two == one:
                answer += 1
    return answer
  
# 33: MIDDLE ELEMENT OF ARRAY
def middle_elem_array(array):
    array.sort()
    answer = array[len(array)//2]
    return answer
  
# 34: STRING in STRING
def solution(str1, str2):
    if str2 in str1:
        answer = 1
    else:
        answer = 2
    return answer

# 35: FIND PAIRS OF NUMBERS WITH MULTIPLY EQUAL TO n
# 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return
def solution(n):
    answer_list = []
    for i in range(1, n+1):
        if n%i==0:
            answer_list.extend([(i, n//i)])
    answer = len(answer_list)
    return answer
    
# 36: FIND NUMBER WITH MAX TIMES OF APPEARENCE (최빈값) 
def solution(array):
    num_list = [0] * (max(array) + 1)
    for num in array:
        num_list[num] += 1
    mode = -1
    first_mode = 0
    second_mode = 0
    for index, times in enumerate(num_list):
        if times > first_mode:
            mode = index
            first_mode = times
        elif times == first_mode:
            second_mode = times
    if first_mode != second_mode:
        answer = mode
    else:
        answer = -1
    return answer


# 37: CALCULATE ALL DIGITS OF NUMBER
# n의 각 자리 숫자의 합을 return
def solution(n):
    answer = 0
    n = str(n)
    for i in n:
        answer = answer + int(i)
    return answer


# 38: FIND OUT IF NUMBER IS SQUARE (제곱수)
def solution(n):
    sqrt_num = n ** (1/2)
    if sqrt_num % 1 == 0:
        answer = 1
    else:
        answer = 2
    return answer


# 39: CALCULATE SM OF DIGITS IN STRING
def solution(my_string):
    answer = 0
    for m in my_string:
        if m.isdigit():
            answer += int(m)
    return answer


# 40: REMOVE CONSONANTS
def solution(my_string):
    answer = ''
    vowels = 'aeiou'
    for m in my_string:
        if m not in vowels:
            answer += m
    return answer
