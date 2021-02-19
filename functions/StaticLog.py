# -*- coding: utf-8 -*-
# @File   : StaticLog
# @Author : penson <penson@penson.top>
# @Email: decentpenson@gmail.com
# @Date   : 2021/2/19 11:45
from functions.functions import *


class StaticLog:
    def __init__(self,dir_list,log_path,save_path):
        self.dir_list = dir_list
        self.log_path = log_path
        self.save_path = save_path

    def static_log(self):
        print(f"save it in {self.save_path}")
        for i in self.dir_list:
            file = f"{self.log_path}\\{i}"
            file_time = get_filetime(file)
            with open(file, 'r', encoding='utf-8') as f:
                text = f.read()
                finding(text, file_time, self.save_path)

    def finding(self):
        for i in self.dir_list:
            file = f"{self.log_path}\\{i}"
            file_time = get_filetime(file)
            where_ip(self.save_path, file_time)
