#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Date : 2024/8/1 下午4:42
Author : StarSink
File : 华住会签到.py
cron :30 8 * * *
new Env('华住会签到')
host : https://appgw.huazhu.com/
export hzhck = "userToken=1b1e*********;" 如果嫌麻烦直接把整个Cookie弄上去就可以了 多账号&分开
"""
from datetime import datetime, timedelta
from time import sleep
import requests
import os
import sys
import random
import notify
import time

sleep_time = [1, 5]

cookies = ""
if cookies == "":
    if os.environ.get("hzhck"):
        cookies = os.environ.get("hzhck")
    else:
        print("请在环境变量填写hzhck的值")
        sys.exit()

list_cookie = cookies.split("&")
n = 1
messages = []

for cookie in list_cookie:
    sleep_t = random.randint(sleep_time[0], sleep_time[1])
    print(f"第{n}个账号随机等待{sleep_t}秒")
    sleep(sleep_t)

    if cookie == "":
        break

    current_timestamp = int(time.time())

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 14; 2106118C Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.188 Mobile Safari/537.36 XWEB/1260079 MMWEBSDK/20240501 MMWEBID/5617 MicroMessenger/8.0.50.2701(0x28003255) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wx286efc12868f2559',
        'Cookie': cookie
    }

    params = {
        'date': str(current_timestamp),
    }

    try:
        response = requests.get('https://appgw.huazhu.com/game/sign_in', params=params, headers=headers)
        r = response.json()
        if r['code'] == 200:
            msg = f"第{n}个账号签到成功：获得积分 {r['content']['point']} 积分"
            print(msg)
            messages.append(msg)
        elif r['code'] == 5004 and r['message'] == "今日已签到":
            msg = f"第{n}个账号：{r['message']}"
            print(msg)
            messages.append(msg)
        else:
            msg = f"第{n}个账号签到异常：{r['message']}"
            print(msg)
            messages.append(msg)
    except Exception as e:
        error_msg = f"第{n}个账号签到失败：{str(e)}"
        print(error_msg)
        messages.append(error_msg)

    try:
        response_points = requests.get('https://appgw.huazhu.com/game/sign_header', headers=headers)
        r_points = response_points.json()
        if r_points['code'] == 200:
            total_points = r_points['content']['memberPoint']
            msg = f"第{n}个账号总积分：{total_points} 积分"
            print(msg)
            messages.append(msg)
        else:
            msg = f"第{n}个账号查询总积分异常：{r_points['message']}"
            print(msg)
            messages.append(msg)
    except Exception as e:
        error_msg = f"第{n}个账号查询总积分失败：{str(e)}"
        print(error_msg)
        messages.append(error_msg)

    try:
        sign_value_list = r_points['content']['signValueList']
        tomorrow_point = None
        tomorrow = datetime.now() + timedelta(days=1)
        tomorrow_date = tomorrow.strftime("%m.%d").lstrip('0').replace('.0', '.')
        for sign_info in sign_value_list:
            if sign_info['date'] == tomorrow_date:
                tomorrow_point = sign_info['point']
                break
        if tomorrow_point is not None:
            msg = f"第{n}个账号明天可获取积分：{tomorrow_point} 积分"
        else:
            msg = f"第{n}个账号未找到明天的积分信息"
        print(msg)
        messages.append(msg)
    except Exception as e:
        error_msg = f"第{n}个账号查询明天积分失败：{str(e)}"
        print(error_msg)
        messages.append(error_msg)

    n += 1

final_message = "\n".join(messages)
notify.send("华住会签到", final_message)
