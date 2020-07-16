ans = 43
min, max = 0, 100
while True:
    guess = int(input('請在%d~%d之間猜一數字:' % (min, max)))
    if guess > ans:
        max = guess
    elif guess < ans:
        min = guess
    else:
        print('恭喜答對了')
        break
