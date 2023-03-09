import sqlite3

class users:
    def __init__(self,tablename="Users",UserId="UserId",Fullname="FullName",UserName="UserName",Password="Password",Email="Email"):
        self.tablename = tablename
        self.UserId = UserId
        self.FullName = Fullname
        self.UserName = UserName
        self.Password = Password
        self.Email = Email
        self.Location = "DataBase\\UserDB.db"
        
        
        conn=sqlite3.connect(self.Location)
        print("Opened database successfully")
        str = "CREATE TABLE IF NOT EXISTS " + self.tablename + "(" + self.UserId + " " + "INTEGER PRIMARY KEY AUTOINCREMENT ,"
        str += " " + self.FullName + " TEXT    NOT NULL ,"
        str += " " + self.UserName + " TEXT    NOT NULL ,"
        str += " " + self.Password + " TEXT    NOT NULL ,"
        str += " " + self.Email + " TEXT)"
        conn.execute(str)
        conn.commit()
        conn.close()


    def insert_user(self, FullName, UserName, Password):
        conn = sqlite3.connect(self.Location)
        str_insert = f"INSERT INTO {self.tablename} ({self.FullName},{self.UserName},{self.Password})VALUES('{FullName}','{UserName}','{Password}')"
        conn.execute(str_insert)
        conn.commit()
        conn.close()
        return "Record created successfully"

    def check_user_by_Username_and_Password(self, UserName, password):
        conn=sqlite3.connect(self.Location)
        strsql = "SELECT * FROM " + self.tablename + " WHERE " + self.UserName + "=" + "'" + str(UserName) + "'" + " AND " + self.Password + "=" + "'" +str(password) + "'"
        cursor = conn.execute(strsql)
        row=cursor.fetchall()
        if row:
            return True
        else:
            return False
        conn.commit()
        conn.close()

    def check_user_by_Username(self, UserName):
        conn=sqlite3.connect(self.Location)
        strsql = "SELECT * FROM " + self.tablename + " WHERE " + self.UserName + "=" + "'" + str(UserName) + "'"
        cursor = conn.execute(strsql)
        row=cursor.fetchone()
        conn.commit()
        conn.close()
        print(row)
        if row:
            return True
        else:

            return False
        

    def delete_by_UserName(self, UserName):
        try:
            conn = sqlite3.connect(self.Location)
            str_delete = "DELETE from " + self.tablename + " where " + self.UserName + "=" + "'" + str(UserName) + "'"
            conn.execute(str_delete)
            conn.commit()
            conn.close()
            print("User Deleted successfully")
            return "Success"
        except:
            return "Failed to delete user"

    def UpdateEmailByUserName(self,Email,UserName):
        try:
            conn = sqlite3.connect(self.Location)
            str_update = f"UPDATE {self.tablename} Set {self.Email} = '{Email}' WHERE {self.UserName} = '{UserName}'"
            print(str_update)
            conn.execute(str_update)
            conn.commit()
            conn.close()
            print("User updated successfully")
            return "Success"
        except:
            return "Failed to update user"

    def GetEmailByUserName(self,UserName):
        try:
            conn=sqlite3.connect(self.Location)
            strsql = "SELECT * FROM " + self.tablename + " WHERE " + self.UserName + "=" + "'" + str(UserName) + "'"
            cursor = conn.execute(strsql)
            row=cursor.fetchone()
            conn.commit()
            conn.close()
            if row[4]:
                return "Exists"
            else:
                return "None"
        except Exception as e:
            print(e)
    
    def ChangePassword(self,Password,UserName):
        try:
            conn = sqlite3.connect(self.Location)
            str_update = f"UPDATE {self.tablename} Set {self.Password} = '{Password}' WHERE {self.UserName} = '{UserName}'"
            conn.execute(str_update)
            conn.commit()
            conn.close()
            print("Password changed successfully")
            return "Success"
        except:
            return "Failed to change password"

if __name__ == "__main__":
    u = users()
    #u.check_user_by_Username_and_Password("2Aura2","12345")
    #u.insert_user("David Jvania", "2Aura","12345")
    #u.check_user_by_Username("2Aura2")
    u.GetEmailByUserName("2Aura2")