"""
階乘函式
0! = 1
1! = 1
2! = 1*2
3! = 1*2*3
n! = 1*2*3*(n-1)*n
"""

# if 3!
sum = 1
for i in range(1, 3+1):
    sum = sum * i
print(sum)

# if 2!
sum = 1
for i in range(1, 2+1):
    sum = sum * i
print(sum)

# if 1!
sum = 1
for i in range(1, 1+1):
    sum = sum * i
print(sum)

def factorial(num):
    if num < 0:
        return -1
    elif num == 0 or num == 1:
        return 1
    else:
        sum = 1
        for i in range(1, num+1):
            sum = sum * i
        return sum

cal_fac = factorial(5)
print(cal_fac)