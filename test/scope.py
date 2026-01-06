# 作用域scope
# 在函式內修改全域變數
x = 100


def func():
    global x
    x = 200
    print("func內的x:", x)


func()
print("func外的x:", x)


# 嵌套函式與nonlocal
def outer():
    num = 23

    def inner():
        nonlocal num  # 指定使用outer()的num變數，而非建立新的區域變數
        num = 45
        print("inner()內的num:", num)

    inner()
    print("outer()內的num:", num)


outer()
