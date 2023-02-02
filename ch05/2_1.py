"""
跳出本次迴圈: continue

while (判斷式):
      # 執行程式
      continue
"""

"""
設計一個程式, 可讓使用者輸入一個區間
程式必須顯示出在此區間內的所有3的倍數
"""

a = int(input("input a : "))
b = int(input("input b : "))

while(a <= b):
    a = a + 1
        
    if(a%3 != 0):
        continue;
    print(a);
