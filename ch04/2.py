"""
if (條件式):
  程式區塊
#若條件成立, 則執行該程式區塊
"""
a = 50;

if(a%2 == 0):
  print("a is even")

"""
米勒百貨公司周年慶, 
公司決定在周年慶期間對消費超過2000元的顧客打7折,
請設計一個收銀台程式, 輸入顧客購買金額後, 
再計算實際要付的錢
"""

pay = int(input("Input total pay: "));

if(pay > 2000.):
  pay = pay * 0.7;


print("the actual pay: {0}".format(pay));

"""
創建一個商品動態清單，它接受使用者的輸入購買數量，最後顯示總金額
價目表如下:
可樂 30 元
綠茶 25 元
義大利麵 80 元 
啤酒 50 元
果汁 45 元
泡麵 55 元
消費超過2000元的顧客打7折,
請設計一個收銀台程式, 輸入顧客購買金額後, 
再計算實際要付的錢
"""