import random

while True:
    n = random.randint(1, 100)
    print(n)
    # 若 n 等於 11 的倍數就停止 (break)
    if n % 11 == 0:
        break
