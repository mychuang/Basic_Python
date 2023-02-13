"""
def functionName(引數):
    程式區塊
    return 回傳值
"""

"""
寫一自訂function f(),計算某一整數的n次方 
"""

def f(a, n):
    print(a**n)

    # 迴圈做法
    # 指數 => 變數自己乘幾次
    # ex: 5**3 = 5*5*5
    # i=1: 5*5 = 25
    # i=2: 25*5 = 125
    
    k = a
    for i in range(1, n):
        a  = a * k
        print(a)
    
    return a

f(5, 3)
