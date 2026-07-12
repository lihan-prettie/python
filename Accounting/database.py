import sqlite3
DB_NAME = "accounting.db"

# SQLite資料庫連線
def get_db_connection():
    return sqlite3.connect(DB_NAME)

#建立資料表
def initialize_database():
    """初始化資料庫，如果資料表不存在就新增資料表"""
    connection = get_db_connection() #呼叫資料庫連線
    cursor = connection.cursor() #建立資料庫內建游標功能

    #用游標執行sql指令建立資料表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id integer primary key autoincrement,
            name text not null,
            amount real not null,
            tag text not null,
            date text default (datetime('now', 'localtime'))
        )
    ''')

    connection.commit()
    connection.close()
    print("資料表 expenses 建立完成")
