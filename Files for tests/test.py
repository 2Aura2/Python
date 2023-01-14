import tkinter
from tkinter import *
import sys
sys.path.insert(1,'D://School Project//Python//DataBase_Codes')
import UserDB

server_data = UserDB.users().check_user_by_Username_and_Password("2Aura2","12345")
print(server_data)








