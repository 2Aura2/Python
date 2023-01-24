import sqlite3

class hashes:
    def __init__(self,tablename="Hashes",HashId="HashId",Hash="Hash"):
        self.tablename = tablename
        self.HashId = HashId
        self.Hash = Hash
        self.Location = "DataBase\\Virus_HashDB.db"
        
        
        conn=sqlite3.connect(self.Location)
        print("Opened database successfully")
        str = "CREATE TABLE IF NOT EXISTS " + self.tablename + "(" + self.HashId + " " + "INTEGER PRIMARY KEY AUTOINCREMENT ,"
        str += " " + self.Hash + " TEXT    NOT NULL)"
        conn.execute(str)
        conn.commit()
        conn.close()


    def insert_Hash(self, Hash):
        conn = sqlite3.connect(self.Location)
        str_insert = f"INSERT INTO {self.tablename} ({self.Hash})VALUES('{Hash}')"
        conn.execute(str_insert)
        conn.commit()
        conn.close()
        return "Record inserted successfully"




VH = hashes()
