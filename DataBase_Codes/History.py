import sqlite3

class users:
    def __init__(self,tablename="History",HistoryId="HistoryId",Start="Start",End="End",FindorNot="FindorNot", Solution="Solution"):
        self.tablename = tablename
        self.HistoryId = HistoryId 
        self.Start = Start 
        self.End = End
        self.FindorNot = FindorNot
        self.Solution = Solution
        
        conn=sqlite3.connect('DataBase\HistoryDB.db')
        print("Opened database successfully")
        str = "CREATE TABLE IF NOT EXISTS " + self.tablename + "(" + self.historyId + " " + "INTEGER PRIMARY KEY AUTOINCREMENT ,"
        str += " " + self.Start + " TEXT    NOT NULL ,"
        str += " " + self.End + " TEXT    NOT NULL ,"
        str += " " + self.FindorNot + " TEXT    NOT NULL ,"
        str += " " + self.Solution + " TEXT    NOT NULL)"
        conn.execute(str)
        conn.commit()
        conn.close()