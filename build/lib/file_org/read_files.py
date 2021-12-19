# -*- coding: utf-8 -*-
import os, time

class files:
    def __init__(self, path, name, year, month):
        self.name  = name
        self.year  = year
        self.month = month
    def print_file(self):
        print(self.name + " " + str(self.year) + "/" + str(self.month) )

def get_folder_files(is_path):
    """Get a thought."""
    lv_files = os.listdir(is_path)

    for lv_file in lv_files:
        list = [] 
        lv_path_file = is_path + lv_file
        lv_time_data = time.gmtime(os.path.getatime(lv_path_file))
        o_file = files(is_path, lv_file, lv_time_data.tm_year,lv_time_data.tm_mon)
        list.append(o_file)
    return list


if __name__ == '__main__':
    lv_path = 'C:\\Dev\\temp\\'
    lv_files = get_folder_files(lv_path)
    print( ">File list:" )
    
    for lv_file in lv_files:
        print("1")
        lv_file.print_file( )
