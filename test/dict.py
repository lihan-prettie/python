# 字典 以 key:value 的方式儲存資料，透過 key 快速存取 value。
handCream = {
    "brand": "rituals...",
    "scent": "sakura",
    "price": 300,
    "name": "櫻花護手霜",
    "color": "白色",
    "abc": "abc",
}
print(handCream["name"])

# 新增
handCream["weight"] = "70ml"
# 修改
handCream["price"] = 350
handCream.update({"expiry_date": "2025-12-31"})
# 刪除
handCream.pop("abc")
del handCream["color"]
# 查詢
print(handCream.get("name", "護手霜"))
print(handCream.keys())
print(handCream.values())
print(handCream.items())
