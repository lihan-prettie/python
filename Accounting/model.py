from database import get_db_connection

def add_expense(name, amount, tag):
    """修增消費紀錄"""
    connetion = get_db_connection()
    cursor = connetion.cursor()
    """使用 ? 佔位符的寫法，資料庫會自動把變數當作「純文字/純數值」處理"""
    cursor.execute(
        "insert into expenses(name, amount, tag) values (?,?,?)",
        (name, amount, tag)
    )

    connetion.commit()
    connetion.close()

def get_all_expense():
    """取得所有消費紀錄"""

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "select id, name, amount, tag, date from expenses"
    )
    #fetchall()會將查詢出來的每一橫列資料取出並列成一個list會傳
    rows = cursor.fetchall()

    conn.close()
    return rows