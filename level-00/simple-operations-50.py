# 51: FIND NUMBER THAT CAN BE DIVIDED TO n
def solution(n, numlist):
    answer = []
    for num in numlist:
        if num%n==0:
            answer.append(num)
    return answer


# 52: UPPER TO LOWER, LOWER TO UPPER
def solution(my_string):
    answer = ''
    for m in my_string:
        if m.isupper():
            answer += m.lower()
        else:
            answer += m.upper()
    return answer


# 53: TRIANGLE WITH *
n = int(input())
answer = ''
for i in range(1, n+1):
    print('*' * i)
    

# 54: GROWTH OF BACTERIA
# 처음 세균의 마리수 n과 경과한 시간 t가 매개변수로
# 주어질 때 t시간 후 세균의 수를 return
def solution(n, t):
    answer = 0
    for i in range(1, t+1):
        answer = n*2
        n = answer
    return answer


# 55: decryption of message
# 암호화된 문자열 cipher에서 code의 배수 번째 글자만 진짜 암호
def solution(cipher, code):
    answer = ''
    for i in range(code, len(cipher)+1):
        if i%code == 0:
            answer += cipher[i-1]
    return answer

# 56: ROCK (0), PAPER(5), SCISSORS(2)
def solution(rsp):
    answer = ''
    for i in rsp:
        if i =='2':
            answer += '0'
        elif i == '0':
            answer += '5'
        else:
            answer += '2'
    return answer

# 57: ORDER ONLY DIGITS IN STRING
def solution(rsp):
    answer = ''
    for i in rsp:
        if i =='2':
            answer += '0'
        elif i == '0':
            answer += '5'
        else:
            answer += '2'
    return answer

# 58: GET MAX NUMBER AND ITS INDEX
def solution(array):
    answer = [0, 0]
    for i in range(len(array)):
        if array[i] > answer[0]:
            answer[0] = array[i]
            answer[1] = i
    return answer

# 59: FIND NUMBERS THAT CAN DIVIDE n
def solution(n):
    answer = []
    for i in range(1, n+1):
        if n%i==0:
            answer.append(i)
    answer.sort()
    return answer
