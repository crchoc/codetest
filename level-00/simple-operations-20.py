# 11: calculate angle type
def angle_type(angle):
    if angle > 0 and angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif angle > 90 and angle < 180:
        answer = 3
    elif angle == 180:
        answer = 4
    return answer
  
# 12: calculate sum of even nums
def sum_even(n):
    answer = 0
    for i in range(n+1):
        if i%2==0:
            answer = answer + i
    return answer
  
# 13: calculate average of array
def average_of_array(numbers):
    answer = sum(numbers)/len(numbers)
    return answer

# 14: calculate number of tall people
def num_of_taller_people(array, height):
    answer = 0
    for i in array:
        if i>height:
            answer = answer + 1
    return answer

# 15: CALCULATE PRICE
# 양꼬치 10인분(12000원)에 음료수(2000원) 하나를 서비스로 줌
def price(n, k):
    answer = 0
    if n >= 10:
        k = k - n//10
    answer = n*12000 + k*2000
    return answer
  
# 16: CHANGE ORDER
# num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return
def change_order(num_list):
    answer = []
    for n in range(len(num_list)-1, -1, -1):
        answer.append(num_list[n])
    return answer
  
# 17: CALCULATE TOTAL NUMBER OF SAME Num
# array에 n이 몇 개 있는 지를 return
def total_number_of_n(array, n):
    answer = 0
    for a in array:
        if a == n:
            answer += 1
    return answer
  
# 18: LENGTH of STRING ELEMENT
# 문자열 배열 strlist 각 원소의 길이를 담은 배열 retrun
def str_length(strlist):
    answer = []
    for s in strlist:
        answer.append(len(s))
    return answer
  
# 19: Calculate PIZZA number
# 피자를 일곱 조각으로 잘라 주면 모든 사람이 피자를 
# 한 조각 이상 먹기 위해 필요한 피자의 수를 return
def pizza_number(n):
    if n % 7 == 0:
        answer = n / 7
    else:
        answer = n//7 + 1
    return answer
  
# 20: GET DOT's plane part
# dot이 사분면 중 어디에 속하는지 1, 2, 3, 4 중 하나를 return
def dot_place(dot):
    if dot[0]>0 and dot[1]>0:
        answer = 1
    elif dot[0]<0 and dot[1]>0:
        answer = 2
    elif dot[0]<0 and dot[1]<0:
        answer = 3
    else:
        answer = 4
    return answer
