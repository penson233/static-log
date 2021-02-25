# -*- coding: utf-8 -*-
# @File   : hello
# @Author : penson <penson@penson.top>
# @Email: decentpenson@gmail.com
# @Date   : 2021/2/19 11:40

import os
import re
import time
from openpyxl import Workbook
from collections import Counter
import requests
from prettytable import PrettyTable

# 得到文件创建时间
def get_filetime(file):
    times = os.path.getmtime(file)
    file_time = time.strftime("%Y-%h-%d", time.localtime(times))
    return file_time

#创建目录
def is_path(path):
    isExists = os.path.exists(path)

    if not isExists:
        os.makedirs(path)

    else:
        return None

#保存为表格
def savetable(table,ip,country,province,city,type,count):
    table.add_row([ip,country,province,city,type,count])
    print(table)

#查找日志文件
def find_log(path):
    files = os.listdir(path)
    dir_list = sorted(files,key=lambda x: os.path.getmtime(os.path.join(path,x)))
    return dir_list

#找到日志文件中的ip，请求方式，请求方式的次数，访问的次数
def finding(text,file_time,save_path):
    find_ip = re.compile("(\d+\.\d+\.\d+\.\d+) - -")
    ips = find_ip.findall(text)
    requests = text.split('\n')

    #统计ip地址
    requests_dict={}
    ua_dict = {}

    #保存请求次数
    wb = Workbook()
    ws = wb.active

    #保存ua
    wb_ua = Workbook()
    ws_ua = wb_ua.active

    ws.append(["ip","请求","该请求次数"])
    ws_ua.append(["ip","请求","请求头(ua)"])

    ip_dict = Counter(ips)
    ip_list =ip_dict.most_common(100)
    count_ip={}
    for ip in ip_list:
        count_ip[ip[0]] =ip[1]
        requests_dict[ip[0]] =[]

    for request in requests:
        request_1 = request.split('\"-\"')
        for i in range(0, len(request_1)):
            ua = request_1[len(request_1) - 1]
            request_3 = request_1[0].split('- -')
            if request_3[0].replace(' ', '') in requests_dict:
                if isinstance(requests_dict[request_3[0].replace(' ', '')], list):
                    request_4 = re.sub("\[.*?\]", '', request_3[1])
                    requests_dict[request_3[0].replace(' ', '')].append(request_4)
                    ua_dict[request_4] = ua

    is_path(f"{save_path}\{file_time}")
    is_path(f"{save_path}\{file_time}\ip_static")

    find_ip=[]
    with open(f'{save_path}\{file_time}\ip_static\ip.txt','a+') as f:
        for key in requests_dict:
            counts = dict(Counter(requests_dict[key]))
            for req in counts:
                if key in ua_dict[req] or ua_dict[req] =="":
                    ua_dict[req] ="空"
                ws.append([key, req, counts[req]])
                ws_ua.append([key,req,ua_dict[req]])
                if key not in find_ip:
                    find_ip.append(key)
                    f.write(key+" "+str(count_ip[key])+"\n")



    is_path(f"{save_path}\{file_time}")
    wb.save(f"{save_path}\{file_time}\{file_time}.xls")
    wb_ua.save(f"{save_path}\{file_time}\\ua.xls")


#查询ip位置
def request(ip):
    apikey = "b54b66c16a25d938"

    url = "https://api.binstd.com/ip/location?appkey={}&ip={}"
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
    }

    newurl=url.format(apikey,ip)
    res = requests.get(url=newurl,headers=header)
    json = res.json()['result']
    country=json['country'] if json['country']!=None else "空"
    province =json['province'] if json['country']!=None else "空"
    city=json['city'] if json['country']!=None else "空"
    type =json['type'] if json['type']!=None else "空"
    return country,province,city,type

#列出ip
def iplist(save_path,file_time):
    with open(f"{save_path}\{file_time}\ip_static\ip.txt",'r') as f:
        ip_numbers=f.readlines()

    ip_dict={}
    with open(f"{save_path}\{file_time}\ip_static\\found_ip.txt",'a+') as f:

        for i in ip_numbers:
            ips=i.replace('\n','').split(' ')
            for i in range(len(ips)):
                ip_dict[ips[0]]=ips[1]
                f.write(ips[0]+"\n")

    return ip_dict

#查询ip地址
def where_ip(save_path,file_time):
    list=[]
    ip_dict = iplist(save_path,file_time)
    i=1
    j=1


    table = PrettyTable()
    table.field_names=["ip","国家","省份","城市","归属","访问次数"]

    for key in ip_dict:
        try:
            country,province,city,type=request(key)
            # print(key,country,province,city,ip_dict[key])
            list.append([key,country,province,city,type,ip_dict[key]])
            savetable(table,key,country,province,city,type,ip_dict[key])
            time.sleep(0.1)
        except:
            print(f"{key} is error")

    wb_ip=Workbook()
    ws_ip=wb_ip.active
    ws_ip.append(["ip","国家","省份","城市","归属","访问次数"])
    for i in list:
        ws_ip.append([i[0],i[1],i[2],i[3],i[4],i[5]])

    wb_ip.save(f"{save_path}\{file_time}\ip请求次数统计.xls")

