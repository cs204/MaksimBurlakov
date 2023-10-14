coin = 50
while coin > 0:
    print("Нужная сумма:", coin)
    user_input = int(input("Вставьте монету: "))
    if user_input in [50, 20, 10, 5]:
        if user_input >= coin:
            excess = user_input - coin
            print("Ваша сдача:", excess)
        coin -= user_input
