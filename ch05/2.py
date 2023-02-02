"""
跳出本次迴圈: continue

while (判斷式):
      # 執行程式
      continue
"""

#顯示 1 - 10, 但不顯示7
a = 0

while(a < 10):
    a = a + 1
        
    if(a == 7):
        continue
    print("a = {0} ".format(a));
    