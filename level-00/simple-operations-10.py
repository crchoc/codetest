# 1: sum of two numbers
def sum_nums(num1, num2):
    answer = num1 + num2
    return answer

# 2: subtraction of nums
def subtraction_nums(num1, num2):
    answer = num1 - num2
    return answer

# 3: multiply two nums
def multiply_nums(num1, num2):
    answer = num1 * num2
    return answer

# 4: find int part of division of two nums
def int_part(num1, num2):
    answer = num1 // num2
    return answer

# 5: divide two nums, multiply by 1000, get int part
def solution(num1, num2):
    answer = int(num1 / num2 * 1000)
    return answer
  
# 6: compare two nums
def compare_nums(num1, num2):
    if num1==num2:
        answer = 1
    else:
        answer = -1
    return answer

# 7: fractional numbers (answer[0] - top, answer[1] - bottom)
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

# 8: create array from an array
def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i*2)
    return answer
  
# 9: remainder of division
def remainder(num1, num2):
    answer = num1%num2
    return answer
  
# 10: calculate year of birth
def year_of_birth(age):
    answer = 2022 - age + 1
    return answer
