import sqlite3
import numpy

class history:
    def __init__(self,tablename="History",HistoryId="HistoryId",Start="Start",End="End",FindorNot="FindorNot", Solution="Solution", UserId="UserId"):
        self.tablename = tablename
        self.HistoryId = HistoryId 
        self.Start = Start 
        self.End = End
        self.FindorNot = FindorNot
        self.Solution = Solution
        self.UserId = UserId
        self.Location = 'DataBase\\HistoryDB.db'
        
        conn=sqlite3.connect(self.Location)
        print("Opened database successfully")
        str = "CREATE TABLE IF NOT EXISTS " + self.tablename + "(" + self.HistoryId + " " + "INTEGER PRIMARY KEY AUTOINCREMENT ,"
        str += " " + self.Start + " TEXT    NOT NULL ,"
        str += " " + self.End + " TEXT    NOT NULL ,"
        str += " " + self.FindorNot + " TEXT    NOT NULL ,"
        str += " " + self.Solution + " TEXT    NOT NULL ,"
        str += " " + self.UserId + " INTEGER    NOT NULL)"
        conn.execute(str)
        conn.commit()
        conn.close()
        
        
        
    def AddScan(self, Start, End, FindorNot, Solution, UserId):
        conn = sqlite3.connect(self.Location)
        str_insert = f"INSERT INTO {self.tablename} ({self.Start},{self.End},{self.FindorNot},{self.Solution},{self.UserId})VALUES('{Start}','{End}','{FindorNot}','{Solution}','{UserId}')"
        conn.execute(str_insert)
        conn.commit()
        conn.close()
        return "Scan added successfully"
    
    def get_scan_by_start_end(self,Start,End):
        try:
            conn = sqlite3.connect(self.Location)
            strsql = f"SELECT * from {self.tablename} where {self.Start} = '{str(Start)}' And {self.End} = '{str(End)}'"
            cursor = conn.execute(strsql)
            row = cursor.fetchone()
            scan_data = str(row[1],row[2],row[3],row[4])
            print("Scan data: " + str(scan_data))
            conn.commit()
            conn.close()
            return scan_data
        except:
            print("Failed to find Scan")
            return False
        

    def get_scan_by_UserId(self,UserId):
        try:
            conn = sqlite3.connect(self.Location)
            str_info = f"SELECT * FROM {self.tablename} WHERE {self.UserId}='{str(UserId)}' ORDER BY UserId DESC LIMIT 5"
            cursor = conn.execute(str_info)
            row = cursor.fetchall()
            print(type(row))
            print(row)
            arr = ','.join(map(str, row))
            print(type(arr))
            print(arr)
            letters_to_remove = "()' "
            for char in letters_to_remove:
                arr = arr.replace(char, "")
            print(type(arr))
            print(arr)
            arr = arr.split(",")
            print(type(arr))
            print(arr)
            conn.commit()
            conn.close()
            return arr
        except:
            print("Failed to find Scan")
            return False
        
        
    def delete_by_start(self, Start):
        try:
            conn = sqlite3.connect(self.Location)
            str_delete = "DELETE from " + self.tablename + " where " + self.Start + "=" + "'" + str(Start) + "'"
            conn.execute(str_delete)
            conn.commit()
            conn.close()
            print("Scan Deleted successfully")
            return "Success"
        except:
            return "Failed to delete Scan" 
        
h = history()
#h.AddScan("3","3","3","3","8")
#x = h.get_scan_by_UserId(8)
#print(x)