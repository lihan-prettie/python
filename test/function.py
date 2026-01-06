# 函數
# 預設參數的函數
def greet(name="guest"):
    print(f"Hello, {name}!")


greet()
greet("Alice")  # 傳入自訂參數


# 傳入不定數量參數
def sum_all(*num):
    return sum(num)


print(sum_all(1, 2, 3))


def bmi(height, weight):
    return weight / (height ** 2)