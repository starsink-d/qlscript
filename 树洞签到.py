#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Date : 2024/7/29 下午6:31
Author : StarSink
File : 树洞签到.py
cron : * * * * *
new Env('树洞签到')
""" 
from time import sleep
import requests
import os
import sys
import random
import notify

# 设置随机等待时间范围
sleep_time = [1, 10]

# 从环境变量中获取cookies，如果环境变量中没有设置，则使用代码中指定的值
cookies = ""
if cookies == "":
    if os.environ.get("sdck"):
        cookies = os.environ.get("sdck")
    else:
        print("请在环境变量填写sdck的值")
        sys.exit()

# 将多个cookie分割成列表
list_cookie = cookies.split("&")
n = 1

# 逐个处理每个cookie
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
            notify.send("树洞签到", msg)
        elif r['ret'] == 0 and "已经签到过了" in r['msg']:
            msg = f"第{n}个账号：{r['msg']}"
            print(msg)
            notify.send("树洞签到", msg)
        else:
            msg = f"第{n}个账号签到异常：{r['msg']}"
            print(msg)
            notify.send("树洞签到", msg)
    except Exception as e:
        error_msg = f"第{n}个账号签到失败：{str(e)}"
        print(error_msg)
        notify.send("树洞签到", error_msg)
    
    n += 1
