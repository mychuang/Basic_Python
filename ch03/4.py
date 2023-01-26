"""
創建一個商品動態清單，它接受使用者的輸入購買數量，最後顯示總金額
價目表如下:
可樂 30 元
綠茶 25 元
義大利麵 80 元
啤酒 50 元
果汁 45 元
泡麵 55 元
"""


cola_num = int(input("input cola "))
green_tea_num = int(input("input green tea "))
pasta_num = int(input("input pasta "))
bear_num = int(input("input bear "))
juice_num = int(input("input juice "))
instant_noodle_num = int(input("input instant noodle "))

cola = 30
green_tea = 25
pasta = 80
bear = 50
juice = 45
instant_noodle = 55

pay = cola*cola_num + green_tea*green_tea_num + pasta*pasta_num + bear*bear_num + juice*juice_num + instant_noodle*instant_noodle_num

print(pay)