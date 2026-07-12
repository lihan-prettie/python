import database
import model
import view

def run_app():
    #程式啟動時要先初始化資料庫
    database.initialize_database()

    #系統主迴圈
    while True:
        view.show_menu() #顯示主選單
        choice = view.get_menu_choice() #取得使用者選項

        if choice == '1':
            #取得輸入
            name, amount, tag = view.add_expense_data()
            #寫入資料庫
            model.add_expense(name, amount, tag)
            print(f"\n 成功新增消費紀錄：花費 {amount} 元購買「{name}」({tag})")
        
        elif choice == '2':
            expense = model.get_all_expense()
            view.show_expenses(expense)
        elif choice == '0':
            print("\n 感謝使用記帳系統，下次見！")
            break

        else:
            print("\n 輸入錯誤！請輸入編號 0, 1 或 2")