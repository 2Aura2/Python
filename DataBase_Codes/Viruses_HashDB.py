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


    def insert_Hash(self,path):
        with open(path, 'r') as f:
            Hash_list = [line.strip() for line in f]
        conn = sqlite3.connect(self.Location)
        for i in range(len(Hash_list)):
            Hash = Hash_list[i]
            print(Hash)
            str_insert = f"INSERT INTO {self.tablename} ({self.Hash})VALUES('{Hash}')"
            conn.execute(str_insert)
            conn.commit()
        conn.close()
        return "Record inserted successfully"

    def select_all_hashes(self):
        try:
            conn = sqlite3.connect(self.Location)
            str1 = "select*from " + self.tablename
            print(str1)
            cursor = conn.execute(str1)
            rows = cursor.fetchall()
            arr_hashes = []
            for row in rows:
                str_rows = row[1]
                arr_hashes.append(str_rows)
            print(arr_hashes)
            return arr_hashes
        except:
            return False


VH = hashes()
#VH.insert_Hash("D:\\School Project\\Python\\Files for tests\\virushash.txt")
#VH.select_all_hashes()