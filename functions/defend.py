# -*- coding: utf-8 -*-
# @File   : defend
# @Author : penson <penson@penson.top>
# @Email: decentpenson@gmail.com
# @Date   : 2021/3/29 22:32
import re


def blacklist_find(req):

    if sqlfind(req):
        return "sql"
    if xssfind(req):
        return "xss"
    if ssrffind(req):
        return "ssrf"
    if directoryfind(req):
        return "brute"
    if functionforphp_find(req):
        return "php"






def sqlfind(req):
    sqlregexp='|'
    with open('./blacklist/sql.txt','r') as f:
        list = f.readlines()

    regexp =sqlregexp.join(list).replace(')','\\)').replace('(','\\(').replace('\n','')
    if search(regexp,req):
        return True
    else:
        return False


def xssfind(req):
    xssregexp='|'
    with open('./blacklist/xss.txt','r') as f:
        list = f.readlines()

    regexp=xssregexp.join(list).replace('\n','')
    if search(regexp,req):
        return True
    else:
        return False

def ssrffind(req):
    ssrfregexp='|'
    with open('./blacklist/ssrf.txt','r') as f:
        list = f.readlines()

    regexp = ssrfregexp.join(list).replace('.','\\.').replace('\n','')

    if search(regexp,req):
        return True
    else:
        return False

def directoryfind(req):
    diregexp='|'
    with open('./blacklist/directory.txt','r') as f:
        list = f.readlines()

    regexp = diregexp.join(list).replace('.','\\.').replace('\n','')

    if search(regexp,req):
        return True
    else:
        return False

def functionforphp_find(req):
    functionregexp='|'
    with open('./blacklist/function_for_php.txt','r') as f:
        list = f.readlines()

    regexp = functionregexp.join(list).replace('(','\\(').replace(')','\\)').replace('\n','')

    if search(regexp,req):
        return True
    else:
        return False

def search(regexp,req):
    finding= re.compile(regexp,re.I)
    found = finding.search(req)
    if found:
        return True
    else:
        return False


if __name__ == '__main__':
    f="/config.php.bak'"
    print(sqlfind(f))

