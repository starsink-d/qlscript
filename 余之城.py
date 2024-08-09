#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Date : 2024/8/5 下午12:36
Author : StarSink
File : 余之城.py
cron : * * * * *
new Env('余之城生活广场')
host: https://crmwx.chongbang.com 抓请求头中的Authorization ，整个放进环境变量中 多账号&分开
"""

from time import sleep
import requests
import os
import sys
import random
import notify

sleep_time = [1, 5]

yzcck = ""

if yzcck == "":
    if os.environ.get("yzcck"):
        yzcck = os.environ.get("yzcck")
    else:
        print("请在环境变量填写yzcck的值")
        sys.exit()

list_yzcck = yzcck.split("&")
n = 1
messages = []

for yzcck in list_yzcck:
    sleep_t = random.randint(sleep_time[0], sleep_time[1])
    print(f"第{n}个账号随机等待{sleep_t}秒")
    sleep(sleep_t)

    if yzcck == "":
        break

    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.50(0x18003236) NetType/4G Language/zh_CN',
        'xweb_xhr': '1',
        'buildingid': 'YH01',
        'Authorization': yzcck
    }

    try:
        response = requests.get('https://crmwx.chongbang.com:52311/api/VipInfo/Sign', headers=headers)
        r = response.json()
        if r['success']:
            msg = f"第{n}个账号签到成功：获得积分 {r['data']['socialpoint']} 积分，总积分 {r['data']['totalsocialpoint']} 积分"
            print(msg)
            messages.append(msg)
        else:
            if r['msg'] == "行为礼包超过限制":
                msg = f"第{n}个账号今日已签到,无需重复签到，防止黑号"
            else:
                msg = f"第{n}个账号签到失败：{r['msg']}"
            print(msg)
            messages.append(msg)
    except Exception as e:
        error_msg = f"第{n}个账号签到请求失败：{str(e)}"
        print(error_msg)
        messages.append(error_msg)

    n += 1

final_message = "\n".join(messages)
notify.send("余之城签到", final_message)
