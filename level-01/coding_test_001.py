# 1: 약수의 합
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    return answer
  
# 2: 짝수와 홀수
def solution(num):
    if num % 2 == 0:
        answer = 'Even'
    else:
        answer = 'Odd'
    return answer
  
# 3: 배열의 평균값
def solution(arr):
    answer = sum(arr)/len(arr)
    return answer
  
# 4: 자릿수의 합
def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer
  
# 5: 자연수 뒤집어 배열로 만들기
def digit_reverse(n):
    answer = list(map(int, reversed(str(n))))
    return answer
  
# 6: Count 'p' and 'y' in dtring
def solution(s):
    s = s.lower()
    p = s.count('p')
    y = s.count('y')
    print(p, y)
    if p == y:
        answer = True
    else:
        answer =  False
    return answer

# 7: 배열 내 divisor로 나눔이 가능한 원소 가져오기
def solution(arr, divisor):
    answer = sorted([a for a in arr if a % divisor == 0]) or [-1]
    return answer

# 8: 수와 부호를 가져와서 합 계산 (나아님)
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

# 9: 4 혹은 6인 길이의 문자열이 숫자로만 되어있는지 확인
def solution(s):
    answer = s.isdigit() and len(s) in (4, 6)
    return answer

