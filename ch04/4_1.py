"""
超級製作人:
你是一個電視台的主管, 你將設定周一至周日的電視節目, 清單如下:
週一: 鬼滅之刃
週二: 航海王
週三: 咒術迴戰
週四: 七龍珠超
週五: 我的英雄學院
週六: 新聞
週日: 新聞

請設計一個查詢平台, 讓使用者輸入 1 - 7 來代表週一至週日, 來查詢節目
"""

show = ["Demon Slayer Blade", "One Piece", 
        "Jujutsu Kaisen", "Dragon ball supper",
        "My Hero Academia", "news" ]
day = int(input("week = (1-7): "))

if day == 1:
    print(show[0])
elif day == 2:
    print(show[1])
elif day == 3:
    print(show[2])
elif day == 4:
    print(show[3])
elif day == 5:
    print(show[4])
elif day == 6 or day == 7:
    print(show[5])
else:
    print("error")