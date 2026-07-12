def show_menu():
    """顯示主選單"""
    print("\n" + "=" * 30)
    print("      💰 簡單記帳系統 💰")
    print("=" * 30)
    print(" 1. 新增消費紀錄")
    print(" 2. 顯示所有消費紀錄")
    print(" 0. 離開系統")
    print("=" * 30)

def get_menu_choice():
    #取得選單編號
    choice = input("請輸入功能編號 (0-2):").strip()
    return choice

def add_expense_data():
    #新增使用者的消費內容
    name = input("請輸入消費名稱 :").strip()

    #金額需要確定是數字
    while True:
        try:
            amount = float(input("請輸入消費金額 :").strip())
            if amount < 0 :
                print("消費金額不可小於0")
                continue
            break
        except ValueError:
            print("請輸入有效的數字金額")
    
    tag = input("請輸入消費分類").strip()
    return name, amount, tag

def show_expenses(expense):
    """顯示所有消費紀錄"""
    if not expense:
        print("暫無消費紀錄")
        return
    
    print("\n" + "-" * 50)
    # ^-10 代表靠左對齊，寬度 10。^8 代表置中對齊。這能讓表格在終端機中整齊排列。
    print(f"{'編號':<6}{'消費名稱':<12}{'金額':<8}{'標籤':<8}{'日期':<20}")
    print("-" * 50)

    for row in expense:
        #row 是一個tuple所以可以直接解包
        id, name, amount, tag, date = row
        print(f"{id:<6}{name:<12}{amount:<8}{tag:<8}{date:<20}")
    print("-" * 50)
