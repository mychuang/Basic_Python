"""
- 巢狀結構:
  if condition a1:
    #<若 condition a1 為真, 則執行此區塊>
    if condition b:
      #<若 condition b 為真, 則執行此區塊>
    else:
      #<若 condition b 為假, 則執行此區塊>
    
  elif condition a2:
    #<若 condition a2 為真, 則執行此區塊>
    if condition c:
      #<若 condition c 為真, 則執行此區塊>
    else:
      #<若 condition c 為假, 則執行此區塊>
      
  else:
    #<若 a1 & a2 皆為假, 則執行此區塊>
"""

"""
超級製作人2:
你是一個電視台的主管, 你將根據年齡層，設定周一至周日的電視節目, 清單如下:

週一: 
 18歲以下: 關於我轉生變成史萊姆這檔事 
 18歲以上(含): 鬼滅之刃 
週二: 航海王
週三: 
 18歲以下: 咒術迴戰
 18歲以上(含): 從零開始的異世界生活 
週四: 七龍珠超
週五: 我的英雄學院
週六: 新聞
週日: 新聞

請設計一個查詢平台, 讓使用者輸入 1 - 7 來代表週一至週日, 來查詢節目
"""

show = ["關於我轉生變成史萊姆這檔事", "航海王", "咒術迴戰", "七龍珠超", "我的英雄學院", "新聞" ]
show18 = ["鬼滅之刃", "從零開始的異世界生活"]
day = int(input("week = (1-7): "))
age = int(input("age: "))

if day == 1:
    if age >= 18:
        print(show18[0])
    else:
        print(show[0])
elif day == 2:
    print(show[1])
elif day == 3:
    if age >= 18:
        print(show18[1])
    else:
        print(show[2])
elif day == 4:
    print(show[3])
elif day == 5:
    print(show[4])
elif day == 6 or day == 7:
    print(show[5])
else:
    print("error")