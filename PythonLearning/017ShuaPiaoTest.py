import urllib.parse
import urllib.request
import json
import re
# 请求头信息
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip',
    'Accept-Language': 'zh-CN',
    'Connection': 'keep-alive',
    'Content-Length': '16',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'www.dingnf.com',
    'Origin': 'http://www.dingnf.com',
    'Referer': 'http://www.dingnf.com/active/wxws_s',
    'User-Agent': 'Mozilla/4.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

# post表单网址
url = "http://www.dingnf.com/active/wxws_t"
params = {'ids': ['22', '22', '22']}
r = requests.post(url=url, data=params, headers=headers, proxies=proxies)
