import urllib.request
import  urllib.parse
response = urllib.request.urlopen('http://ent.cnr.cn/gd/20170913/W020170913267348133258.jpg')
html_img = response.read()
# html_img = html_img.decode('utf-8')
# print(html_img)

# with open('flower.jpg','wb') as firstImage:
#     firstImage.write(html_img)

# 有道翻译



url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

head = {}
head['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'

data = {
    'i':'中国',
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':'1505704505075',
    'sign':'7e5f88efc9febd040fc619d808e59514',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_CLICKBUTTION',
    'typoResult':'true'
}
data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url,data,head)
html2 = urllib.request.urlopen(req)
res = html2.read().decode('utf-8')
print(res)