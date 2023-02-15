"""
費式數列 - 遞迴函式
1, 1, 2, 3, 5, 8, 13 ...

f(0) = 1
f(1) = 1
f(2) = f(2-1) + f(2-2)
f(3) = f(3-1) + f(3-2)
f(n) = f(n-1) + f(n-2)
"""

def feb(num):
    if num < 0:
        print("error")
    
    if num == 0 or num == 1:
        return 1
    else:
        return feb(num-1) + feb(num-2)
    
    
for i in range(10):
    print(feb(i))