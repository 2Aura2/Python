import sqlite3

class history:
    def __init__(self,tablename="History",HistoryId="HistoryId",Start="Start",End="End",FindorNot="FindorNot", Solution="Solution"):
        self.tablename = tablename
        self.HistoryId = HistoryId 
        self.Start = Start 
        self.End = End
        self.FindorNot = FindorNot
        self.Solution = Solution
        
        conn=sqlite3.connect('DataBase\HistoryDB.db')
        print("Opened database successfully")
        str = "CREATE TABLE IF NOT EXISTS " + self.tablename + "(" + self.HistoryId + " " + "INTEGER PRIMARY KEY AUTOINCREMENT ,"
        str += " " + self.Start + " TEXT    NOT NULL ,"
        str += " " + self.End + " TEXT    NOT NULL ,"
        str += " " + self.FindorNot + " TEXT    NOT NULL ,"
        str += " " + self.Solution + " TEXT    NOT NULL)"
        conn.execute(str)
        conn.commit()
        conn.close()
        
        
        
    def AddScan(self, Start, End, FindorNot, Solution):
        conn = sqlite3.connect('DataBase\HistoryDB.db')
        str_insert = f"INSERT INTO {self.tablename} ({self.Start},{self.End},{self.FindorNot},{self.Solution})VALUES('{Start}','{End}','{FindorNot}','{Solution}')"
        conn.execute(str_insert)
        conn.commit()
        conn.close()
        return "Scan added successfully"
    
    def get_scan_by_start_end(self,Start,End):
        try:
            conn = sqlite3.connect("DataBase\HistoryDB.db")
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
        
        
    def delete_by_UserName(self, Start):
        try:
            conn = sqlite3.connect('DataBase\HistoryDB.db')
            str_delete = "DELETE from " + self.tablename + " where " + self.Start + "=" + "'" + str(Start) + "'"
            conn.execute(str_delete)
            conn.commit()
            conn.close()
            print("Scan Deleted successfully")
            return "Success"
        except:
            return "Failed to delete Scan"
        
        
h = history()