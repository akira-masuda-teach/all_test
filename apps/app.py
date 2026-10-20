me = 100
you = 100

print("初期HP")
print("私のHPは", me)
print("敵のHPは", you)

while(True):

    print()
    print("1:攻撃、2:回復")
    input_val = int(input("数値を入力："))

    print("")
    if input_val == 1:
        you = you - 10
        print("あなたは攻撃した！")
        print("敵に10のダメージ")

    elif input_val == 2:
        me += 10
        print("あなたは回復した！")
        print("HPが10回復した")
    else:
        print("なにもできていないよ！")

    print()
    print("私のHPは",me)
    print("敵のHPは", you)
    if you <= 0:
        print("敵を倒した")
        break


