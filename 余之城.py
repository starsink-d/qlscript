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

    user_agents = [
        "Mozilla/5.0 (Linux; Android 13; V2148A Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160117 MMWEBSDK/20240404 MMWEBID/8833 MicroMessenger/8.0.49.2600(0x28003137) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
        "Mozilla/5.0 (Linux; Android 12; NOH-AL00 Build/HUAWEINOH-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160117 MMWEBSDK/20240404 MMWEBID/6916 MicroMessenger/8.0.49.2600(0x28003136) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64",
        "Mozilla/5.0 (Linux; Android 14; V2307A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160117 MMWEBSDK/20240301 MMWEBID/4922 Mozilla/5.0 (iPad; CPU OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x1800302d) NetType/WIFI Language/zh_CN",
        "Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x1800302d) NetType/WIFI Language/zh_CN",
        "Mozilla/5.0 (iPad; CPU OS 15_7_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.29(0x18001d38) NetType/WIFI Language/zh_CN",
        "Mozilla/5.0 (iPad; CPU OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003127) NetType/WIFI Language/zh_CN",
        "Mozilla/5.0 (iPad; CPU OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003129) NetType/WIFI Language/zh_CN",
        "Mozilla/5.0 (Linux; Android 13; 23049RAD8C Build/TKQ1.221114.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160083 MMWEBSDK/20230303 MMWEBID/4466 MicroMessenger/8.0.34.2340(0x2800225F) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003127) NetType/WIFI Language/zh_CN",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003127) NetType/WIFI Language/zh_CN",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x18003030) NetType/4G Language/zh_CN",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.42(0x18002a32) NetType/4G Language/zh_CN",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.48(0x1800302c) NetType/WIFI Language/zh_CN",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309092b) XWEB/8461 Flue",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090a13) XWEB/9117 Flue",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.884.400 QQBrowser/9.0.2524.400",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090819) XWEB/9129 Flue",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63040026)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090926) XWEB/9079 Flue"
    ]

    random_user_agent = random.choice(user_agents)
    print(f"随机选择的User-Agent: {random_user_agent}")

    headers = {
        'User-Agent': random_user_agent,
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
