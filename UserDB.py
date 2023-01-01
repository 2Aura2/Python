import sqlite3

class users:
    def __init__(self,tablename="Users",UserId="UserId",Fullname="FullName",UserName="UserName",Password="Password"):
        self.tablename = tablename
        self.UserId = UserId
        self.FullName = Fullname
        self.UserName = UserName
        self.Password = Password
        
        conn=sqlite3.connect('UserDB.db')
        print("Opened database successfully")
        str = "CREATE TABLE IF NOT EXISTS " + self.tablename + "(" + self.UserId + " " + "INTEGER PRIMARY KEY AUTOINCREMENT ,"
        str += " " + self.FullName + " TEXT    NOT NULL ,"
        str += " " + self.UserName + " TEXT    NOT NULL ,"
        str += " " + self.Password + " TEXT    NOT NULL)"
        conn.execute(str)
        conn.commit()
        conn.close()


    def insert_user(self, FullName, UserName, Password):
        conn = sqlite3.connect('UserDB.db')
        str_insert = f"INSERT INTO {self.tablename} ({self.FullName},{self.UserName},{self.Password})VALUES('{FullName}','{UserName}','{Password}')"
        conn.execute(str_insert)
        conn.commit()
        conn.close()
        return "Record created successfully"





u = users()