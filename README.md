# static_log

this is for your web log.
it can help you to static ip,request,ip's amount,request's amount.

you must install Python Install third party modules brefore you use it!

## pip3 install -r requirements.txt

## python3 main.py -l (your log path) -s (you want to save and default is: it will generate in directory main.py in)

# for example

## python3 main.py -l P:\日志文件分析\static_log\12\log -s output


it will save as log's generate times
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210219174640511.png)


it is ip requests
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210219174632868.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NvcFJvbWVv,size_16,color_FFFFFF,t_70)


it is the number of ip

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210219174648387.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NvcFJvbWVv,size_16,color_FFFFFF,t_70)

it is the ua of ip

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210219174656720.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NvcFJvbWVv,size_16,color_FFFFFF,t_70)

and it will generrate ip.txt it found ,you can use nmap to Batch scanning by foundip.txt

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210219174700824.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NvcFJvbWVv,size_16,color_FFFFFF,t_70)
