# coding=utf-8
"""
* Project name: LaiXuanZuo.py
* Author : 罗申申 luoenen
* E-mail：luoenen@github.com
* WeChat：19939374645
*
"""
import requests
import time
import json
import sys
from user_info import readUser
from utils import system_header,system_cookie

reload(sys)
sys.setdefaultencoding('utf8')

"""
进行选座的主函数说明：
在选座系统中，共分为三个参数：

AAAAA 代表图书馆楼层
BB CC 代表座位坐标
例如：我在图书馆八楼：即是 11117 12，14
"""
def Today(weChat_header, weChat_cookie, floor_ID, seat_X,seat_Y):
    # 图书馆楼层URL
    url_library = "http://wechat.laixuanzuo.com/index.php/reserve/layout/libid=%s.html&%s"%(floor_ID,str(int(time.time())))
    # 开抢URL---------------------------------------重点------------------------------ ：每次抢座，{Unknown} 值都会变，这是由其HTML中JavaScript 次次更改
    # ---------------------------------------  JavaScript 代码中有一段验证  location.href = t.url 进行修改参数，因此我无法解决这个问题，特此开源，共同努力
    url_begin   = "http://wechat.laixuanzuo.com/index.php/reserve/get/libid=%s&{Unknown}=%s,%s&yzm="%(floor_ID, seat_X,seat_Y)
    requests.adapters.DEFAULT_RETRIES = 5
    rs = requests.Session()
    rs.keep_alive = False
    try:
        print "即将进行系统验证："
        time.sleep(1)
        url_weChat = "http://wechat.laixuanzuo.com/index.php/reserve/index.html?f=wechat"
        url_verify = "http://wechat.laixuanzuo.com/index.php/misc/verify.html"
        rs.get(url_weChat, timeout=10, headers=weChat_header, cookies=weChat_cookie)
        rs.get(url_verify, timeout=10, headers=weChat_header, cookies=weChat_cookie)
        print "系统验证身份顺利通过"
    except Exception as e:
        print(u"[E]: 系统验证出错，脚本选择继续执行 %s" % repr(e))
        time.sleep(1)
    try:
        print "即将准备进入系统模拟楼层"
        time.sleep(1)
        response = rs.get(url_library, timeout=10, headers=weChat_header, cookies=weChat_cookie)
        time.sleep(1)
        print "成功进入该楼层"
        print "该楼层网络地址："+url_library
        time.sleep(1)
        print "打印系统源码：选择忽略"
    except Exception as e:
        time.sleep(1)
        print(u"[E]: 进入图书馆楼层选座出错 %s" % repr(e))
    else:
        if response.status_code == 200:
            print(u"[I]: 进入自习室成功")
        else:
            print(u"[I]: 进入自习室失败")
    try:
        print "系统即将进行选座："
        time.sleep(1)
        print "系统再次进行识别身份认证，身份信息："
        print "正在操作系统用户身份："+weChat_cookie["wechatSESS_ID"]+"：身份识别无误!"
        url_verify = "http://wechat.laixuanzuo.com/index.php/misc/verify.html"
        rs.get(url_verify, timeout=10, headers=weChat_header, cookies=weChat_cookie)
        response = rs.get(url_begin, timeout=10, headers=weChat_header, cookies=weChat_cookie)
        get_token = json.loads(response.text)
        print "确认选座二维码如下:"
        print get_token["url"]
        print "确认选座二维码如上:"
        time.sleep(1)
        print "打印系统选座信息："
        time.sleep(1)
        print response.text
    except Exception as e:
        print(u"[E]: 确认选座出错 %s" % repr(e))
    else:
        if response.status_code == 200:
            print(u"[I]: 图书馆选座：第 %s 层图书馆 %s,%s 号位置抢座成功!" % (floor_ID, seat_X,seat_Y) + "")
        else:
            print(u"[I]: 图书馆选座：第 %s 层图书馆 %s,%s号位置抢座失败!未知原因" % (floor_ID, seat_X,seat_Y) + "")




if __name__ == "__main__":
    print ("*"*150)
    print "\n*********** 基于Python2.7 第一代选座系统 for河南财经政法大学(HeNan University of Economics and Law) 图书馆选座系统准备运行 v1.0.0\n"
    print ("*" * 150)
    time.sleep(1)
    readUser()
    index = 0
    while True:
        index +=1
        try:
            # 图书馆标号，八楼 11117
            floor_ID = 11117
            # 36号坐标 12，14
            seat_X = 12
            seat_Y = 14
            Today(system_header, system_cookie, floor_ID, seat_X, seat_Y)
        except Exception as e:
            print(u"[E]: 抢座出错 %s" % repr(e))
        break

    raw_input(u"\n[I]: please press any key to continue...")