# 61: CREATE ARRAY
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer
  
# 62: NEAREST NUMBER
def solution(array, n):
    emp = []
    array.sort()
    for i in array:
        emp.append(abs(n-i))
    answer = [array[emp.index(min(emp))]]
    if len(answer) > 1:
        answer = min(answer)
    else:
        answer = answer[0]
    return answer
  
# 63: EMERGENCY ORDER (my version)
def solution(emergency):
    answer = []
    sorted_emer = sorted(emergency, reverse=True)
    emer_dict = dict()
    for i in range(len(sorted_emer)):
        emer_dict[sorted_emer[i]] = i+1
    for j in emergency:
        answer.append(emer_dict[j])
    return answer
  
# 63: EMERGENCY ORDER (best version)
def solution(emergency):
    answer = [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]
    return answer
  
# 64: SOLDIERS (not my version)
def solution(hp):
    answer = hp//5 + (hp%5)//3 + (hp%5)%3
    return answer
  
# 65: DICE BOX
# box size, n - number of dots
def solution(box, n):
    answer = int(box[0] // n) * int(box[1] // n) * int(box[2] // n)
    return answer
  
# 66: COMPOSITE NUMBER (not mine)
def solution(n):
    answer = 0
    emp = []
    for i in range(2, n+1):
        for j in range(1, i+1):
            if i % j == 0:
                emp.append(i)
        if emp.count(i) >= 3:
            answer += 1
    return answer
  
# 67: NUMBER OF k BETWEEN i AND j
def solution(i, j, k):
    answer = 0
    for num in range(i, j+1):
        for digit in str(num):
            if str(digit) == str(k):
                answer += 1
    return answer
  
# 68: LIST OF CHARs THAT ARE ONLY ONE TIME (not mine)
def solution(s):
    answer = ''.join(sorted(i for i in s if s.count(i) == 1))
    return answer
  
# 69: NUMBER OF DIGIT 7 IN ALL ELEMENTS
def solution(array):
    answer = 0
    for i in array:
        for j in str(i):
            if j == '7':
                answer += 1
    return answer
  
# 70: SUM OF BINARY NUMBERS (not mine)
def solution(bin1, bin2):
    answer = format((int(bin1, 2)+int(bin2, 2)), 'b')
    return answer
