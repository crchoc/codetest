# 81: Character POINT PLACE
def solution(keyinput, board):
    col = board[0]
    row = board[1]
    answer = [0,0]
    for i in keyinput:
        if i == "left" and answer[0]-1 >= -(col // 2):
            answer[0] -= 1
        elif i == "right" and answer[0]+1 <= (col // 2):
            answer[0] += 1
        elif i == "up" and answer[1]+1 <= (row // 2):
            answer[1] += 1
        elif i == "down" and answer[1]-1 >= -(row // 2):
            answer[1] -= 1
    return answer
    
# 82: FIND SIDE FOR TRIANGLE
def solution(sides):
    answer = (sorted(sides)[0] * 2) - 1
    return answer
    
# 83: LOGIN STATUS
def solution(id_pw, db):
    for i in db:
        if i[0] == id_pw[0] and i[1] == id_pw[1]:
            answer = 'login'
        elif i[0] == id_pw[0] and i[1] != id_pw[1]:
            answer = 'wrong pw'
        elif i[0] != id_pw[0] and i[1] != id_pw[1]:
            answer = 'fail'
    return answer
    
# 84: 유한소수
from math import gcd
def solution(a, b):
    b //= gcd(a,b)
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    if b == 1: 
        answer = 1
    else:
        answer = 2
    return answer

# 85: CHICKEN COUPON
def solution(chicken):
    answer = 0
    while chicken >= 10:
        div = chicken // 10
        mod = chicken % 10
        answer += div
        chicken = div + mod
    return answer

# 86: SPECIAL SORT
def solution(numlist, n):
    answer = sorted(numlist, key=lambda x: (abs(n-x), -x))
    return answer

# 87: RANK OF STUDENTS
def solution(score):
    answer = []
    avg = []
    for s in score:
        avg.append(sum(s)/len(s))
    sort_avg = sorted(avg, reverse=True)
    for i in avg:
        answer.append(sort_avg.index(i)+1)     
    return answer

# 88: CHANGE DIGIT 3
# new num: 1->1, 2->2, 3->4, 4->5, 5->7,
# 6->8, 7->10, 8->11, 9->14, 10->16
def solution(n):
    answer = 0
    for i in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer

# 89: OX quiz
def solution(quiz):
    answer = ['O' if eval(each.replace('=', '==')) else 'X' for each in quiz]
    return answer

# 90: NEXT NUMBER
def solution(common):
    num = common[1] - common[0]
    if common[1] + num == common[2]:
        answer = common[len(common)-1] + num
    else:
        num = common[1] // common[0]
        answer = common[len(common)-1] * num
    return answer
