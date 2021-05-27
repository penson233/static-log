# -*- coding: utf-8 -*-
# @File   : main
# @Author : penson <penson@penson.top>
# @Email: decentpenson@gmail.com
# @Date   : 2021/2/19 12:12
import argparse
from functions.functions import find_log
from functions.StaticLog import StaticLog


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="static_log")
    parser.add_argument('-l', type=str, help="the_log_position")
    parser.add_argument('-s', type=str, default="./", help="the_position_you_want_to_save")

    args = parser.parse_args()
    log_path = args.l
    save_path = args.s

    print('''
         _        _   _        _             
     ___| |_ __ _| |_(_) ___  | | ___   __ _ 
    / __| __/ _` | __| |/ __| | |/ _ \ / _` |
    \__ \ || (_| | |_| | (__  | | (_) | (_| |
    |___/\__\__,_|\__|_|\___| |_|\___/ \__, |
                                       |___/ 
        ''')

    dir_list = find_log(log_path)
    Static =StaticLog(dir_list,log_path,save_path)
    Static.static_log()
    print(f"success all save  ！！ it is in {save_path}")
    print("start find ip please wait")
    Static.finding_ip()

