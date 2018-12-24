# coding=utf-8
"""
* Project name: LaiXuanZuo.py
* Author : 罗申申 luoenen
* E-mail：luoenen@github.com
* WeChat：19939374645
*
"""
import sys
import time

reload(sys)
sys.setdefaultencoding('utf8')

"""
浏览器标识，用于向来选座系统发出伪装请求
"""
system_header = {
'Host': "wechat.laixuanzuo.com",
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.901.400 QQBrowser/9.0.2524.400',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,image/wxpic,image/sharpp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.8,en-us;q=0.6,en;q=0.5;q=0.4'
}

"""
在微信中，微信内置浏览器识别用户，只有一个Cookie 即是：wechatSESS_ID 其用于保存用户所有信息
Hm_下标识，表示当前时间，lvt 标识刷新次数，每次刷新都会记录时间戳，我用当前时间表示
"""
system_cookie = dict(FROM_TYPE="weixin",
              wechatSESS_ID="683f7b19439bdf64e8bbbe39ed618402",
			  Hm_lvt_7838cef374eb966ae9ff502c68d6f098=str(int(time.time())),
			  Hm_lpvt_7838cef374eb966ae9ff502c68d6f098=str(int(time.time())))