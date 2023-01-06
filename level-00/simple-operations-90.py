# Character POINT PLACE
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
    
# FIND SIDE FOR TRIANGLE
def solution(sides):
    answer = (sorted(sides)[0] * 2) - 1
    return answer
    
# LOGIN STATUS
def solution(id_pw, db):
    for i in db:
        if i[0] == id_pw[0] and i[1] == id_pw[1]:
            answer = 'login'
        elif i[0] == id_pw[0] and i[1] != id_pw[1]:
            answer = 'wrong pw'
        elif i[0] != id_pw[0] and i[1] != id_pw[1]:
            answer = 'fail'
    return answer
    
# 
