import re
import os
import time
from openpyxl import Workbook
from collections import Counter


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



    for key in requests_dict:
        counts = Counter(requests_dict[key]).most_common(30)
        for count in counts:
            ws.append([key,count[0],count[1],count_ip[key]])

    wb.save(f"{save_path}\{file_time}.xls")

    print("success save  ！！")

def statics(dir_list,log_path,save_path):
    for i in dir_list:
        file = f"{log_path}\\{i}"
        times =os.path.getmtime(file)
        file_time =time.strftime("%Y-%h-%d",time.localtime(times))
        print(file_time)
        with open(file,'r',encoding='utf-8') as f:
            text = f.read()
            finding(text,file_time,save_path)






if __name__ == '__main__':
    log_path = input("Please enter log path\n")
    dir_list = find_log(log_path)
    save_path = input("It is working,please input the path you want to save:\n")
    statics(dir_list,log_path,save_path)
