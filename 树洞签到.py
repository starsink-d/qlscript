#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Date : 2024/7/29 下午6:31
Author : StarSink
File : 树洞签到.py
cron : * * * * *
new Env('树洞签到')
host : https://helloshudong.com/
"""
from time import sleep
import requests
import os
import sys
import random
import notify

sleep_time = [1, 10]

cookies = ""
if cookies == "":
    if os.environ.get("sdck"):
        cookies = os.environ.get("sdck")
    else:
        print("请在环境变量填写sdck的值")
        sys.exit()

list_cookie = cookies.split("&")
n = 1

all_msgs = []

for cookie in list_cookie:
    sleep_t = random.randint(sleep_time[0], sleep_time[1])
    print(f"第{n}个账号随机等待{sleep_t}秒")
    sleep(sleep_t)
    
    if cookie == "":
        break
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        "Cookie": cookie
    }
    
    qdurl = 'https://hello-shudong.com/user/checkin'
    
    try:
        r = requests.post(qdurl, headers=headers).json()
        if r['ret'] == 1:
            msg = f"第{n}个账号签到成功：{r['msg']}\n剩余流量：{r['traffic']}"
            print(msg)
        elif r['ret'] == 0 and "已经签到过了" in r['msg']:
            msg = f"第{n}个账号：{r['msg']}"
            print(msg)
        else:
            msg = f"第{n}个账号签到异常：{r['msg']}"
            print(msg)
    except Exception as e:
        msg = f"第{n}个账号签到失败：{str(e)}"
        print(msg)
    
    all_msgs.append(msg)
    n += 1

final_msg = "\n\n".join(all_msgs)
notify.send("树洞签到", final_msg)
