# (不可變)tuple元組練習
# week = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")

# # 取值
# print(week[2])

# # tuple解包
# _, *weekday, _ = week
# print(weekday)

# set集合(忽略重複的值)
numbers1 = {2, 2, 5, 8, 5, 8}
numbers2 = {1, 2, 3, 4, 5}
print(numbers1)

# 新增
numbers1.add(1)
print(numbers1)

# 若刪除不存在的值會報錯
numbers1.remove(1)
print(numbers1)

# 若刪除不存在的值不報錯
numbers1.discard(6)
print(numbers1)

print("\n", "-" * 20)
# 交集
print(numbers1 & numbers2)

# 聯集
print(numbers1 | numbers2)

# 差集
print(numbers1 - numbers2)
