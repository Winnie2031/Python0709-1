scores = [100, 90, 80, 70, 60, 50]  # 數組
print(len(scores))  # 數組的元素個數
# 各科列印
for i in range(0, len(scores)):
    print(scores[i])
# 求總分 ?
sum = 0
for i in range(0, len(scores)):
    sum += scores[i]  # 累加
print("總分: %d" % sum)

