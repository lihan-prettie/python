import time
import random

# 倒數計時
for i in range(5, 0, -1):
    print(i, "sec")
    time.sleep(1)
print("times up!")

# while基礎練習
# count = 0
# while count < 5:
#     print("第", count, "次")
#     count += 1

# 九九乘法表
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{i} x {j} = {i*j}", end="\t")
#     print()

# 猜數字遊戲
answer = random.randint(0, 20)
attempt = 0

while True:
    uer_input = input("請輸入0~20的數字:")
    if not uer_input.isdigit():
        print("請輸入數字!")
        continue

    guess = int(uer_input)
    attempt += 1

    if guess == answer:
        print("正確答案!")
        print(f"共猜{attempt}次")
        break
    elif guess > answer:
        print("數字大於答案，請再猜一次")
    else:
        print("數字小於答案，請再猜一次")
