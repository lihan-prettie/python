# list練習

vehicles = ["BMW", "Benz", "Toyota", "Tsuzuki", "123", "789"]
# 增
vehicles.append("456")
vehicles.insert(2, "Subaru")
# 刪
vehicles.remove("123")
vehicles.pop()
del vehicles[4]
# 改
vehicles[4] = "Hendai"
# 查
for vehicle in vehicles:
    print(vehicle)


# 數字串列排序(升冪)
raw_numbers = [1, 8, 7, 9, 4, 6, 3, 5, 2]

asp_num = sorted(raw_numbers)
for num in asp_num:
    print(num, end="  ")
print("\n", "-" * 20)

# 數字串列排序(降冪)
des_num = sorted(raw_numbers, reverse=True)
for num in des_num:
    print(num, end="  ")

# 字串串列排序(依字首字母升冪)
names = ["Peter", "lily", "ann", "charlie"]

asp_names = sorted(names)
for name in asp_names:
    print(name)
print("\n", "-" * 20)

# 字串串列排序(依字首字母降冪)
des_names = sorted(names, reverse=True)
for name in des_names:
    print(name)
print("\n", "-" * 20)

# 自訂字串排序(按照字串長度)
head_names = sorted(names, key=len)
for name in head_names:
    print(name)
print("\n", "-" * 20)

# 自訂字串排序(忽略大小寫排序)
ord_name = sorted(names, key=str.lower)
for name in ord_name:
    print(name)
