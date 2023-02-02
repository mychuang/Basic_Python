"""
跳出整個迴圈: break

  while (判斷式):
      # 執行程式
      break
"""

#顯示 1 - 10, 顯示6即停止
a = 0

while(a < 10):
    a = a + 1

    if(a == 7):
        break;
    print("a = {0}".format(a))
    