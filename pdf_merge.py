import os
from merge_pdf import merge

files_list = []

for i in os.scandir():
    if ".pdf" in i.name:
        files_list.append(i.name)


name_pdf = input("\nNombra el PDF ==> ")


merge.Merge (name_pdf, replace= True).merge_file_list (files_list)