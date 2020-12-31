import re
import os
import time
from openpyxl import Workbook
from collections import Counter
import requests
from prettytable import PrettyTable
import random

#按修改时间排序列出日志文件
def find_log(path):
    files = os.listdir(path)
    dir_list = sorted(files,key=lambda x: os.path.getmtime(os.path.join(path,x)))
    return dir_list

#找到日志文件中的ip，请求方式，请求方式的次数，访问的次数
def finding(text,file_time,save_path):
    find_ip = re.compile("(\d+\.\d+\.\d+\.\d+) - -")
    ips = find_ip.findall(text)
    requests = text.split('\n')
    requests_dict={}
    #保存所有信息
    wb = Workbook()
    ws = wb.active

    ws.append(["ip","请求","请求次数","访问次数"])

    ip_dict = Counter(ips)
    ip_list =ip_dict.most_common(70)
    count_ip={}
    for ip in ip_list:
        count_ip[ip[0]] =ip[1]
        requests_dict[ip[0]] =[]

    for request in requests:
        request_1 = request.split('\"-\"')
        for request_2 in request_1:
            request_3 = request_2.split('- -')
            if request_3[0].replace(' ','') in requests_dict:
                if isinstance(requests_dict[request_3[0].replace(' ','')],list):
                    request_4 = re.sub("\[.*?\]", '', request_3[1])
                    requests_dict[request_3[0].replace(' ','')].append(request_4)

    with open(f'{save_path}\ip.txt','a') as f:
        for key in requests_dict:
            counts = Counter(requests_dict[key]).most_common(30)
            for count in counts:
                ws.append([key,count[0],count[1],count_ip[key]])
                f.write(key+' '+str(count_ip[key])+'\n')



    wb.save(f"{save_path}\{file_time}.xls")





def statics(dir_list,log_path,save_path):
    for i in dir_list:
        file = f"{log_path}\\{i}"
        times =os.path.getmtime(file)
        file_time =time.strftime("%Y-%h-%d",time.localtime(times))
        with open(file,'r',encoding='utf-8') as f:
            text = f.read()
            finding(text,file_time,save_path)


def request(ip):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
    }

    url=f"http://ip-api.com/json/{ip}?lang=zh-CN"
    res = requests.get(url=url,headers=header)
    json = res.json()
    country=json['country']
    province =json['regionName']
    city=json['city']
    if province =="":
        province="无"
    if city =="":
        city="无"

    return country,province,city

def savetable(table,ip,country,province,city,count):
    table.add_row([ip,country,province,city,count])

    print(table)



def iplist(save_path):
    with open(f"{save_path}\ip.txt") as f:
        ip_numbers=f.readlines()

    ip_dict={}
    for i in ip_numbers:
        ips=i.replace('\n','').split(' ')
        for i in range(len(ips)):
            if ips[0] not in ip_dict:
                ip_dict[ips[0]]=ips[1]

    return ip_dict

if __name__ == '__main__':
    log_path = input("Please enter log path\n")
    dir_list = find_log(log_path)
    save_path = input("It is working,please input the path you want to save:\n")
    statics(dir_list,log_path,save_path)
    print(f"success all save  ！！ it is in {save_path}")
    list=[]
    ip_dict = iplist(save_path)
    i=1
    j=1
    table = PrettyTable()
    table.field_names=["ip","国家","省份","城市","访问次数"]
    for key in ip_dict:
        try:
            country,province,city=request(key)
            # print(key,country,province,city,ip_dict[key])
            list.append([key,country,province,city,ip_dict[key]])
            savetable(table,key,country,province,city,ip_dict[key])
            i+=1
            if(i==30*j):
                print("每30个ip一组，请耐心等待~~~")
                time.sleep(60)
                j+=1
            time.sleep(0.1)
        except:
            print(f"{key} is error")

    wb_ip=Workbook()
    ws_ip=wb_ip.active
    ws_ip.append(["ip","国家","省份","城市","访问次数"])
    for i in list:
        ws_ip.append([i[0],i[1],i[2],i[3],i[4]])

    wb_ip.save(f"{save_path}\ip地址.xls")




