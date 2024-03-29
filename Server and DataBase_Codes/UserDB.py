import sqlite3
import traceback
import hashlib


class users:
    def __init__(self,tablename="Users",UserId="UserId",Fullname="FullName",UserName="UserName",Password="Password",Email="Email"):
        self.tablename = tablename
        self.UserId = UserId
        self.FullName = Fullname
        self.UserName = UserName
        self.Password = Password
        self.Email = Email
        self.Location = "..\\DataBase\\UserDB.db"
        
        
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
        try:
            md5_hash_Password = hashlib.md5(Password.encode()).hexdigest()
            conn = sqlite3.connect(self.Location)
            str_insert = f"INSERT INTO {self.tablename} ({self.FullName},{self.UserName},{self.Password})VALUES(?,?,?)"
            cursor = conn.cursor()
            cursor.execute(str_insert,(str(FullName),str(UserName),str(md5_hash_Password),))
            conn.commit()
            conn.close()
            return "User created successfully"
        except Exception as e:
            print("Error:",e)
            return "Error while creating user"

    def check_user_by_Username_and_Password(self, UserName, password):
        try:
            md5_hash_Password = hashlib.md5(password.encode()).hexdigest()
            conn=sqlite3.connect(self.Location)
            strsql = f"SELECT * FROM {self.tablename} WHERE {self.UserName} = ? AND {self.Password} = ?"
            cursor = conn.execute(strsql,(str(UserName), str(md5_hash_Password),))
            row=cursor.fetchall()
            conn.commit()
            conn.close()
            if row:
                return True
            else:
                return False
        except Exception as e:
            print("Error:",e)
            return "Error while checking user"
        

    def check_user_by_Username(self, UserName):
        try:
            conn=sqlite3.connect(self.Location)
            strsql = f"SELECT * FROM {self.tablename} WHERE {self.UserName} = ?" 
            cursor = conn.cursor()
            cursor.execute(strsql, (str(UserName),))
            row=cursor.fetchone()
            conn.commit()
            conn.close()
            if row:
                return True
            else:
                return False
        except Exception as e:
            print("Error:",e)
            return "Error while checking user existence"
        

    def delete_by_UserName(self, UserName):
        try:
            conn = sqlite3.connect(self.Location)
            str_delete = f"DELETE from {self.tablename} WHERE {self.UserName} = ?"
            conn.execute(str_delete,(str(UserName),))
            conn.commit()
            conn.close()
            print("User Deleted successfully")
            return "Success"
        except Exception as e:
            print("Error:",e)
            return "Error while deleting user"

    def UpdateEmailByUserName(self,Email,UserName):
        try:
            conn = sqlite3.connect(self.Location)
            str_update = f"UPDATE {self.tablename} Set {self.Email} = ? WHERE {self.UserName} = ?"
            conn.execute(str_update,(str(Email),str(UserName),))
            conn.commit()
            conn.close()
            print("User updated successfully")
            return "Success"
        except Exception as e:
            print("Error:",e)
            return "Error while updating user"

    def GetEmailByUserName(self,UserName):
        try:
            conn=sqlite3.connect(self.Location)
            strsql = f"SELECT * FROM {self.tablename} WHERE {self.UserName} = ?"
            cursor = conn.execute(strsql,(str(UserName),))
            row=cursor.fetchone()
            conn.commit()
            conn.close()
            if row[4]:
                return "Exists"
            else:
                return "None"
        except Exception as e:
            print("Error:",e)
            return "Error while getting user"

    def GetUserIdByUserName(self,UserName):
        try:
            conn=sqlite3.connect(self.Location)
            strsql = f"SELECT * FROM {self.tablename} WHERE {self.UserName} = ?"
            cursor = conn.execute(strsql,(str(UserName),))
            row=cursor.fetchone()
            conn.commit()
            conn.close()
            if row[0]:
                return row[0]
            else:
                return "None"
        except Exception as e:
            print("Error:",e)
            return "Error while getting user"
    
    def ChangePassword(self,Password,UserName):
        try:
            md5_hash_Password = hashlib.md5(Password.encode()).hexdigest()
            conn = sqlite3.connect(self.Location)
            str_update = f"UPDATE {self.tablename} Set {self.Password} = ? WHERE {self.UserName} = ?"
            conn.execute(str_update,(str(md5_hash_Password), str(UserName),))
            conn.commit()
            conn.close()
            return "Password changed successfully"
        except Exception as e:
            print("Error:",e)
            return "Error while changing password"
        
    def ChangeUserName(self,NewUserName,UserName):
        try:
            conn = sqlite3.connect(self.Location)
            str_update = f"UPDATE {self.tablename} Set {self.UserName} = ? WHERE {self.UserName} = ?"
            conn.execute(str_update,(str(NewUserName),str(UserName),))
            conn.commit()
            conn.close()
            return "UserName changed successfully"
        except Exception as e:
            print("Error:",e)
            return "Error while changing UserName"


if __name__ == "__main__":
    u = users()
    #u.check_user_by_Username_and_Password("1","1")
    #u.insert_user("David Jvania", "2Aura","12345")
    #u.check_user_by_Username("1")
    #u.GetEmailByUserName("2Aura2")
    #u.getall()