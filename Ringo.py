import sqlite3

conn = sqlite3.connect("RingoSQL.db")
cur = conn.cursor()
#conn.execute('''CREATE TABLE CHAT1
#         (ID INT PRIMARY KEY     NOT NULL,
#         CHAT TEXT, 
#          RINGO TEXT);''')

def Boss_Ringo():
    boss = input("Boss:")
    ringo = input("Ringo:")
    cursor = conn.execute ("SELECT MAX(ID)  FROM CHAT1")
    for row in cursor:
        a = row[0]+1
    insert = "INSERT INTO CHAT1 VALUES(%s, '%s','%s' ) "%(a , boss, ringo) 
    conn.execute (insert) 
    conn.commit()
def Player_Ringo():
    player = input("Player: ")
    select = "SELECT * FROM CHAT1 WHERE CHAT = '%s' "%player
    cursor = conn.execute (select)
    conn.commit()
    for row in cursor:
        print("Tadashi Ringo:", row[2])
def Ringo():
    pass
input_ = input(">>>")
while input_ :
    if input_ == "Admin":
        Boss_Ringo()
    elif input_ == "Player":
        Player_Ringo()
