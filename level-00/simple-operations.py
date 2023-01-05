# sum of two numbers
def sum_nums(num1, num2):
    answer = num1 + num2
    return answer

# subtraction of nums
def subtraction_nums(num1, num2):
    answer = num1 - num2
    return answer

# multiply two nums
def multiply_nums(num1, num2):
    answer = num1 * num2
    return answer

# find int part of division of two nums
def int_part(num1, num2):
    answer = num1 // num2
    return answer

# divide two nums, multiply by 1000, get int part
def solution(num1, num2):
    answer = int(num1 / num2 * 1000)
    return answer
  
# compare two nums
def compare_nums(num1, num2):
    if num1==num2:
        answer = 1
    else:
        answer = -1
    return answer

# fractional numbers (answer[0] - top, answer[1] - bottom
def fracnums(denum1, num1, denum2, num2):
    answer = []
    top = denum1*num2 + denum2*num1
    bottom = num1*num2
    n = math.gcd(top, bottom)
    if n==1:
        answer = [top, bottom]
    else:
        answer = [top/n, bottom/n]
    return answer

# create array from an array
def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i*2)
    return answer
  
# remainder of division
def remainder(num1, num2):
    answer = num1%num2
    return answer
  
# calculate year of birth
def year_of_birth(age):
    answer = 2022 - age + 1
    return answer

# calculate angle type
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
  
# calculate sum of even nums
def sum_even(n):
    answer = 0
    for i in range(n+1):
        if i%2==0:
            answer = answer + i
    return answer
  
# calculate average of array
def average_of_array(numbers):
    answer = sum(numbers)/len(numbers)
    return answer

# calculate number of tall people
def num_of_taller_people(array, height):
    answer = 0
    for i in array:
        if i>height:
            answer = answer + 1
    return answer

# CALCULATE PRICE
# 머쓱이네 양꼬치 가게는 10인분을 먹으면 음료수 
# 하나를 서비스로 줍니다. 양꼬치는 1인분에 12,000원,
# 음료수는 2,000원입니다. 정수 n과 k가 매개변수로 
# 주어졌을 때, 양꼬치 n인분과 음료수 k개를 먹었다면 
# 총얼마를 지불해야 하는지 return 하도록 
# solution 함수를 완성해보세요.
def price(n, k):
    answer = 0
    if n >= 10:
        k = k - n//10
    answer = n*12000 + k*2000
    return answer
  
# CHANGE ORDER
# 정수가 들어 있는 배열 num_list가 매개변수로 주어집니다.
# num_list의 원소의 순서를 거꾸로 뒤집은 배열을 
# return하도록 solution 함수를 완성해주세요.
def change_order(num_list):
    answer = []
    for n in range(len(num_list)-1, -1, -1):
        answer.append(num_list[n])
    return answer
  
# CALCULATE TOTAL NUMBER OF SAME Num
# 정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, 
# array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.
def total_number_of_n(array, n):
    answer = 0
    for a in array:
        if a == n:
            answer += 1
    return answer
  
# LENGTH of STRING ELEMENT
# 문자열 배열 strlist 각 원소의 길이를 담은 배열 retrun
def str_length(strlist):
    answer = []
    for s in strlist:
        answer.append(len(s))
    return answer
  
# Calculate PIZZA number
# 피자를 일곱 조각으로 잘라 주면 피자를 나눠먹을 사람의 수 n이 주어질 때, 
# 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return
def pizza_number(n):
    if n % 7 == 0:
        answer = n / 7
    else:
        answer = n//7 + 1
    return answer
  
# GET DOT's plane part
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
  
# PIZZA NUMBER (2)
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
  
# NUMBER of AMERICANO and MONEY
# money최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을
# 순서대로 담은 배열을 return
def nums_and_money(money):
    answer = []
    answer.append(money//5500)
    answer.append( money - answer[0]*5500)
    return answer
  
# CHANGE ORDER OF STRING
# my_string을 거꾸로 뒤집은 문자열을 return
def string_order(my_string):
    answer = ''
    answer = my_string[::-1]
    return answer

# CALCULATE TRIANGLE SIDES
# 세 변으로 삼각형을 만들 수 있다면 1, 만들 수 없다면 2를 return
def check_triangle(sides):
    max_side = max(sides)
    sides.remove(max_side)
    if max_side<sum(sides):
        answer = 1
    else:
        answer = 2
    return answer
  
# CALCULATE EVEN AND ODDS of LIST
# num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return
def even_odd_nums(num_list):
    answer = [0, 0]
    for n in num_list:
        if n%2==0:
            answer[0] += 1
        else:
            answer[1] += 1
    return answer

# LENGTH of MESSAGE
# 글자 한 자 한 자를 가로 2cm 크기로 적으려고 하며, 
# 편지를 가로로만 적을 때, 축하 문구 message를 
# 적기 위해 필요한 편지지의 최소 가로길이를 return 
def message_length(message):
    answer = len(message)*2
    return answer
  
# REMOVE SPECIFIC CHARACTER
# my_string에서 letter를 제거한 문자열을 return
def solution(my_string, letter):
    answer = my_string.replace(letter, '')
    return answer
  

# MAX MULTIPLY in LIST
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return
def max_multiply(numbers):
    answer = 0
    max_n = 0
    for i in range(len(numbers)-1):
        if numbers[i]*numbers[i+1]>max_n:
            answer = numbers[i]*numbers[i+1]
            max_n = answer
    return answer
  
# REPEAT CHRACTERS in STRING
# my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return
def repeat_char(my_string, n):
    answer = ''
    for m in my_string:
        answer += m*n
    return answer
  
# LIST SLICING
# numbers의 num1번 째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을 return
def slicing_list(numbers, num1, num2):
    answer = numbers[num1, num2]
    return answer
  
# ODD nums in REVERSE ORDER
# n 이하의 홀수가 오름차순으로 담긴 배열을 return
def odds_in_reverse(n):
    answer = []
    for i in range(n, 0, -1):
        if i % 2 != 0:
            answer.append(i)
    answer.reverse()
    return answer
  
  
# CALCULATE SAME CHARS IN TWO STRINGS
def same_chars(s1, s2):
    answer = 0
    for one in s1:
        for two in s2:
            if two == one:
                answer += 1
    return answer
  
# MIDDLE ELEMENT OF ARRAY
def middle_elem_array(array):
    array.sort()
    answer = array[len(array)//2]
    return answer
  
# STRING in STRING
def solution(str1, str2):
    if str2 in str1:
        answer = 1
    else:
        answer = 2
    return answer

# FIND PAIRS OF NUMBERS WITH MULTIPLY EQUAL TO n
# 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return
def solution(n):
    answer_list = []
    for i in range(1, n+1):
        if n%i==0:
            answer_list.extend([(i, n//i)])
    answer = len(answer_list)
    return answer
    
# FIND NUMBER WITH MAX TIMES OF APPEARENCE (최빈값) 
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


# CALCULATE ALL DIGITS OF NUMBER
# n의 각 자리 숫자의 합을 return
def solution(n):
    answer = 0
    n = str(n)
    for i in n:
        answer = answer + int(i)
    return answer


# FIND OUT IF NUMBER IS SQUARE (제곱수)
def solution(n):
    sqrt_num = n ** (1/2)
    if sqrt_num % 1 == 0:
        answer = 1
    else:
        answer = 2
    return answer


# CALCULATE SM OF DIGITS IN STRING
def solution(my_string):
    answer = 0
    for m in my_string:
        if m.isdigit():
            answer += int(m)
    return answer


# REMOVE CONSONANTS
def solution(my_string):
    answer = ''
    vowels = 'aeiou'
    for m in my_string:
        if m not in vowels:
            answer += m
    return answer

# FIND NUMBER THAT CAN BE DIVIDED TO n
def solution(n, numlist):
    answer = []
    for num in numlist:
        if num%n==0:
            answer.append(num)
    return answer


# UPPER TO LOWER, LOWER TO UPPER
def solution(my_string):
    answer = ''
    for m in my_string:
        if m.isupper():
            answer += m.lower()
        else:
            answer += m.upper()
    return answer


# TRIANGLE WITH *
n = int(input())
answer = ''
for i in range(1, n+1):
    print('*' * i)
    

# GROWTH OF BACTERIA
# 처음 세균의 마리수 n과 경과한 시간 t가 매개변수로
# 주어질 때 t시간 후 세균의 수를 return
def solution(n, t):
    answer = 0
    for i in range(1, t+1):
        answer = n*2
        n = answer
    return answer


# decryption of message
# 암호화된 문자열 cipher에서 code의 배수 번째 글자만 진짜 암호
def solution(cipher, code):
    answer = ''
    for i in range(code, len(cipher)+1):
        if i%code == 0:
            answer += cipher[i-1]
    return answer

# ROCK (0), PAPER(5), SCISSORS(2)
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
