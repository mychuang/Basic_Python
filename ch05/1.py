"""
若條件符合, 即**持續**執行某段程式碼
  while (判斷式):
      # 執行程式
"""

status = 1
a = 0

while(status == 1):
    a = a + 1;
    print("a = {0}".format(a))
    if(a == 10):
        status = 0

#補充: 可用bool改寫如下
status = True
a = 0
while(status):
    a = a + 1;
    print("a = {0}".format(a))

    if(a == 10):
        status = False