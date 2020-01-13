# encoding:utf-8
import requests
api = "https://sc.ftqq.com/SCU42319T0e58ee2e36a881b575b112dba79d91c75dcca70adf1c4.send"
title = u"博客更新啦~"
content = """
## 刚刚博客有更新，快去看看吧
"""
data = {
   "text":title,
   "desp":content
}
req = requests.post(api,data = data)