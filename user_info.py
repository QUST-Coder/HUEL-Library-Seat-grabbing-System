# coding=utf-8
"""
* Project name: LaiXuanZuo.py
* Author : 罗申申 luoenen
* E-mail：luoenen@github.com
* WeChat：19939374645
*
"""
import json
import requests
from seat_info import My_Seat
from utils import system_header,system_cookie

"""
微信统一标识：WeChatSession_ID，功能请详细阅读utils.py 
"""
WeChatSession_ID = "683f7b19439bdf64e8bbbe39ed618402"

"""
尝试携带Cookies 登录来选座系统（试水）
"""
def readUser():
    dict_openID_SESSID = {}
    """
    来选座系统首页的URL
    """
    url = "http://wechat.laixuanzuo.com/index.php/reserve/index.html?f=wechat"
    try:
        dict_openID_SESSID = json.loads('{"user":"%s,%s"}' % (WeChatSession_ID, My_Seat))
    except Exception as e:
        print(u"[E]: 尝试读取抢座定义信息出错! %s" % repr(e))
    for v in dict_openID_SESSID.values():
        try:
            list_info = v.split(",")
            lens = len(list_info)
            system_cookie["wechatSESS_ID"] = list_info[0].strip()
        except Exception as e:
            print(u"[E]: 尝试验证wechatSESS_ID出错! %s" % repr(e))
    try:
        response = requests.get(url,timeout=10, headers=system_header, cookies=system_cookie)
    except Exception as e:
        print(u"[E]: 尝试进入首页出错 %s" % repr(e))
        return "ERROR"
    else:
        if response.status_code == 200:
            print "成功尝试进入首页"
        else:
            print(u"[E]: 尝试进入首页出错 ")