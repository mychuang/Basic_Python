"""
顯示費氏數列前10個

    pesudo code:

    前兩個數字 = 0
    前一個數字 = 1

    for (10次)
      當前數字 = 前兩個數字 + 前一個數字
    
      更新: 前兩個數字
      更新: 前一個數字
"""

num_pre0 = 0
num_pre1 = 1

print(num_pre0)
print(num_pre1)

for i in range(10):
    num_current = num_pre0 + num_pre1
    print(num_current)
    
    num_pre0 = num_pre1
    num_pre1 = num_current