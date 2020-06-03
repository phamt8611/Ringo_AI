import sqlite3
import sys
import os

conn = sqlite3.connect('RingoSQL.db')
cur = conn.cursor()
#cur.execute ("INSERT INTO NAMES VALUES(1,'BOSS', 19,'Địa Cầu', 0,'Đen', 'Đen', 'Viết truyện, Lập trình máy tính, kiếm tiền', 'Không rõ', 'Sơ cấp lập trình python', 'Chưa có', 'Chưa có', 'Tadashi Ringo') ")
#cur.execute ("INSERT INTO HỆ_THỐNG VALUES(1,  'Xin chào!') ")

#cur.execute("SELECT * FROM NAMES ORDER BY ID ASC")
#cur.execute ("DELETE FROM NAMES Where ID = 2")

#cur.execute("DROP TABLE HỆ_THỐNG")

#conn.execute('''CREATE TABLE HỆ_THỐNG
#         (ID INTERGER AUTO_INCREMENT ,
#         INPUT  TEXT    OT NULL)''')
def SHOW_NAMES(so_cot):
    cursor = conn.execute ("SELECT * FROM NAMES")
    for row in cursor:
        print(row[so_cot])
def HE_THONG():
    #He_Thong_Cursor_ID = conn.execute("SELECT *FROM")
    #He_Thong_Cursor = conn.execute ("INSERT INTO HỆ_THỐNG VALUES() ")
    Boss_Player =  input("Nhập vào: ")
    T_Or_F = bool(Boss_Player)
    print(T_Or_F)
    while T_Or_F == False:
        if T_Or_F == True:
            SHOW_HE
            #Ringo_Player = input("Cái nào là hành động? ")
            T_Or_F = False
#HE_THONG()
print(cur.fetchone())
conn.commit()