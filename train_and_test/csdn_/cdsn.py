import urllib.request
import re

data= urllib.request.urlopen("https://www.csdn.net").read().decode("utf-8")
pat = '"([a-zA-Z]+://[^\s]*)" target="_blank"'
rst = re.compile(pat).findall(data)
for i in range(0,len(rst)):
    try:
        url = rst[i]
        #urllib.request.urlretrieve(url,"/data/tools/pycharm/urllist/"+str(i)+".html")
        urllib.request.urlretrieve(url,"~/Desktop/Work_2018/train_and_test/csdn_/urllist/"+str(i)+".html")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reson"):
            print(e.reason)

