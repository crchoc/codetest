# 21: PIZZA NUMBER (2)
# 피자 조각 수 slice와 피자를 먹는 사람의 수 n이 
# 최소 한 조각 이상 피자를 먹으려면 최소 몇 판의 
# 피자를 시켜야 하는지를 return 
def solution(slice, n):
    answer = 0
    if n % slice == 0:
        answer = n/slice
    else:
        answer = n//slice + 1
    return answer
  
# 22: NUMBER of AMERICANO and MONEY
# money최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을
# 순서대로 담은 배열을 return
def nums_and_money(money):
    answer = []
    answer.append(money//5500)
    answer.append( money - answer[0]*5500)
    return answer
  
# 23: CHANGE ORDER OF STRING
# my_string을 거꾸로 뒤집은 문자열을 return
def string_order(my_string):
    answer = ''
    answer = my_string[::-1]
    return answer

# 24: CALCULATE TRIANGLE SIDES
# 세 변으로 삼각형을 만들 수 있다면 1, 만들 수 없다면 2를 return
def check_triangle(sides):
    max_side = max(sides)
    sides.remove(max_side)
    if max_side<sum(sides):
        answer = 1
    else:
        answer = 2
    return answer
  
# 25: CALCULATE EVEN AND ODDS of LIST
# num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return
def even_odd_nums(num_list):
    answer = [0, 0]
    for n in num_list:
        if n%2==0:
            answer[0] += 1
        else:
            answer[1] += 1
    return answer

# 26: LENGTH of MESSAGE
# 글자 한 자 한 자를 가로 2cm 크기로 적으려고 하며, 
# 편지를 가로로만 적을 때, 축하 문구 message를 
# 적기 위해 필요한 편지지의 최소 가로길이를 return 
def message_length(message):
    answer = len(message)*2
    return answer
  
# 27: REMOVE SPECIFIC CHARACTER
# my_string에서 letter를 제거한 문자열을 return
def solution(my_string, letter):
    answer = my_string.replace(letter, '')
    return answer
  

# 28: MAX MULTIPLY in LIST
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return
def max_multiply(numbers):
    answer = 0
    max_n = 0
    for i in range(len(numbers)-1):
        if numbers[i]*numbers[i+1]>max_n:
            answer = numbers[i]*numbers[i+1]
            max_n = answer
    return answer
  
# 29: REPEAT CHRACTERS in STRING
# my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return
def repeat_char(my_string, n):
    answer = ''
    for m in my_string:
        answer += m*n
    return answer
  
# 30: LIST SLICING
# numbers의 num1번 째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을 return
def slicing_list(numbers, num1, num2):
    answer = numbers[num1, num2]
    return answer
