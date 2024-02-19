import sqlite3

conn = sqlite3.connect('sqlite.db')
cursor = conn.cursor()

ui = """

1- 新增帳號
2- 修改帳號
3- 刪除帳號
4- 顯示帳號

--- --- ---
0- 離開

"""
is_run = True

while is_run:
    cursor.execute('SELECT * FROM `account`;')
    records = cursor.fetchall()

    choose = input(ui + "請輸入您的選擇:")
    print("")
    if choose == "0":
        is_run = False

    elif choose == "1":
        
        name = input("請輸入欲新增的名字:")
        account = input("請輸入欲新增的帳號:")
        password = input("請輸入欲新增的密碼:")
        sql = """
        INSERT INTO account (name,account,password)
        VALUES ({},{},{});
        """.format(name,account,password)
        cursor.execute(sql)
        conn.commit()
        pass

    elif choose == "2":
        row_id = input("請選擇欲修改的資料:")
        name = input("請輸入欲新增的名字:")
        account = input("請輸入欲新增的帳號:")
        password = input("請輸入欲新增的密碼:")
        sql = """
        update account
        set name = {} ,account ={} , password = {}
        where id ={};
        """.format(name,account,password,row_id)
        cursor.execute(sql)
        conn.commit()
        pass

    elif choose == "3":
        row_id = input("請選擇欲刪除的資料:")
        sql = """
        delete from account
        where id = {};
        """.format(row_id)
        cursor.execute(sql)
        conn.commit()
        pass
    elif choose == "4":
        print("目前的帳戶如下")
        for i in records:
            print(i)
        pass
        print("")
        back = input("請輸入任意鍵返回:")
        
cursor.close()
conn.close