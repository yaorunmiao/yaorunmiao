import requests
from pyquery import PyQuery as pq
headers = {
       "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42"
    }
url = "https://www.baidu.com/"
r=requests.get(url,headers=headers)
r.raise_for_status()
r.encoding=r.apparent_encoding
demo = r.text
doc = pq(demo)
i = 1#计数用
for inf in doc.find('.title-content-title').items():
    # print(inf)
    d = pq(inf)
    # print(d("a"))
    p = d("span")
    # span标签里面的内容
    v=p.text()
    # span标签的父亲所有内容
    w=p.parent()
    # 网站链接
    q=w.attr.href
    print(q)
    with open('i:/作业.txt', 'a', encoding=r.apparent_encoding) as f:
        f.write(str(i) + '.')
        f.write(v)
        f.write(q)
        f.write('\n')  # 写入
    i += 1








