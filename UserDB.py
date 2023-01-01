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

    def check_user_by_Username_and_Password(self, UserName, password):
            conn=sqlite3.connect('UserDB.db')
            strsql = "SELECT * FROM " + self.tablename + " WHERE " + self.UserName + "=" + "'" + str(UserName) + "'" + " AND " + self.Password + "=" + "'" +str(password) + "'"
            cursor = conn.execute(strsql)
            row=cursor.fetchall()
            if row:
                return True
            else:
                return False
            conn.commit()
            conn.close()

    def delete_by_UserName(self, UserName):
        try:
            conn = sqlite3.connect('UserDB.db')
            str_delete = "DELETE from " + self.tablename + " where " + self.UserName + "=" + "'" + str(UserName) + "'"
            conn.execute(str_delete)
            conn.commit()
            conn.close()
            print("User Deleted successfully")
            return "Success"
        except:
            return "Failed to delete user"





u = users()
#u.check_user_by_Username_and_Password("2Aura2","12345")
#u.insert_user("David Jvania", "2Aura2","12345")