# 91: SUM OF CONTINUOUS NUMBERS
def solution(num, total):
    average = total // num
    answer = [i for i in range(average - (num-1)//2, average + (num+2)//2)]
    return answer

# 92: FIND SAFE ZONE
import numpy as np
from collections import Counter
def solution(board):
    n = len(board)
    board_padded = np.pad(board, ((1,1), (1,1)), constant_values=-1)
    danger_array = np.pad(board, ((1,1), (1,1)), constant_values=-1)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if board_padded[i][j] == 1:
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        danger_array[x][y] = 1
    danger_list = danger_array.reshape(1,-1).squeeze()
    answer = Counter(danger_list)[0]
    return answer
    
# 93: 웅알이
from itertools import permutations
def solution(babbling):
    answer = 0
    speek = ["aya","ye","woo","ma"]
    word = []
    for i in range(1, len(speek)+1):
        for j in permutations(speek, i):
            word.append(''.join(j))

    for i in babbling:
        if i in word:
            answer += 1
    return answer
    
# 94: LEN OF LINES IN NTHE SAME COORDINATES
def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])

# 95: POLYNOMIAL SUM
def solution(polynomial):
    answer = '0'
    l = polynomial.split("+ ")
    x, num = 0, 0
    for a in l:
        a = a.strip()
        if a[-1] == "x":
            if len(a) == 1:
                x += 1
            else:
                x += int(a[:-1])
        else:
            num += int(a)

    if x == 0:
        return str(num)
    elif num == 0:
        if x == 1:
            return "x"
        return str(x) + "x"
    if x == 1:
        return "x + " + str(num)
    return str(x) + "x + " + str(num)

