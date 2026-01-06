import math as m
import random as r

# 數學模組練習
num = 16
float_num = 7.8
print(f"{num}平方根:{m.sqrt(num)}")
print(f"{num}的立方:{m.pow(num,3)}")
print(f"{float_num}的無條件進位:{m.ceil(float_num)}")
print(f"{float_num}的無條件捨去:{m.floor(float_num)}")
print("圓周率:", m.pi)


letters = ["a", "b", "c", "d", "e"]
numbers = list(range(10))
# 隨機模組練習
print("產生0-100間隨機整數:", r.randint(1, 100))
print("產生1-5間隨機浮點數:", r.uniform(1, 5))
print("在列表中隨機選:", r.choice(letters))
r.shuffle(letters)
print("打亂序列順序後的列表:", letters)
print("隨機取出4個不重複的值:", r.sample(numbers, 4))
