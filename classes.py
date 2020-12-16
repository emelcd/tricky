import os
from colorama import Fore
from beautifultable import BeautifulTable
import string
from random import choice
from time import sleep
# for files in os.scandir():
#     if ".py" in files.name:
#         print(Fore.YELLOW+files.name)
pool =  string.digits 

class Tables:
    def __init__(self, square):
        self.square = square
        self.rows = self.square
        self.columns = self.square
        self.table = self.generate_T()

    def generate_T(self):
        table = BeautifulTable()
        for i in range(self.rows):
            table.rows.append([""]*self.columns)
        self.table = table
        return self.table
        
    def add_content_T(self):
        # self.generate_T(1)
        self.table.rows.header = [Fore.LIGHTYELLOW_EX+choice(pool) for i in range(self.rows)]
        self.table.columns.header = [Fore.LIGHTYELLOW_EX+choice(pool) for i in range(self.columns)]
        # self.table.rows[0] = ["eco"] * self.columns
        matches = []
        # print(self.table)
        a = 0
        x_match = Fore.LIGHTWHITE_EX + "X"
        
        while a<self.columns:
            for i in range(self.columns):
                if self.table.rows.header[a] == self.table.columns.header[i]:
                    # print("match ["+str(a)+"-"+str(i)+"]")
                    self.table.rows[a][i] = x_match
                    matches.append("1")
            a += 1
        print(self.table)
        print(str(len(matches))+ " MATCHES")    

square = int(input("DIME EL LADO: "))
table_1 = Tables(square)
table_1.add_content_T()
