import os
import sys
import re
import csv
import logging
import time
from datetime import datetime
import urllib.request
import urllib.error
import cchardet

class JdInfo(object):

    def __init__(self):
        self.workdir = os.path.dirname(sys.argv[0])
        self.logger = self.initlog()
        self.setting()
        self.shoplist = []
        self.commentcnt = 0

    def initlog(self):
        # 获取logger实例，如果参数为空则返回root logger
        logger = logging.getLogger("WebCrawler")
        # 指定logger输出格式
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(module)s %(funcName)s %(message)s')
        # 文件日志
        filepath = os.path.join(self.workdir, "debug.log")
        file_handler = logging.FileHandler(filepath, "w")
        file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式
        # 为logger添加的日志处理器
        logger.addHandler(file_handler)
        # 指定日志的最低输出级别，默认为WARN级别
        logger.setLevel(logging.INFO)
        logger.info("Start...")
        return logger

    def setting(self, proxy=False):

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"}
        header = []
        for key, value in headers.items():
            header.append((key, value))
        if proxy:
            proxyhd = urllib.request.ProxyHandler({"http": "127.0.0.1:8888"})
            opener = urllib.request.build_opener(proxyhd, urllib.request.HTTPHandler)
        else:
            opener = urllib.request.build_opener()
        opener.addheaders = header
        urllib.request.install_opener(opener)

    def checkwebsite(self, url, timeout=10):
        """
        @检查网页访问情况
        :param url: 网址
        :param timeout: 超时设置
        :return:None或者爬虫对象
        """
        response = None
        try:
            response = urllib.request.urlopen(url, timeout=timeout)
            self.logger.info("【%s】网页[%s]，正在处理..." % (response.getcode(), response.geturl()))
        except urllib.error.URLError as e:
            if hasattr(e, "reason"):
                self.logger.error("访问网页[%s]失败，原因：%s" % (url, e.reason))
            if hasattr(e, "code"):
                self.logger.error(e.code)
        return response

    def encodingdetector(self, html):
        """
        @检查网页编码,以网页标识的编码格式为主
        :param html:网页内容
        :return:网页编码
        """
        coding = cchardet.detect(html)['encoding']
        text = html.decode(coding)
        if text.find('content="text/html;') != -1:
            charset = re.findall(r'content="text/html; charset=\s?(.*?)"', text, re.I)[0]
            if charset.strip().upper() != coding.strip().upper():
                text = html.decode(charset)
        return text

    def getshopname(self, shop):
        """
        :return:商品名称
        """
        pattern = r'<div class="p-name p-name-type-2">.*?<em>(.*?)</em>'
        pname = re.findall(pattern, shop, re.S)
        if pname:
            shopname = re.sub(r'<font class="(.*?)"', "", pname[0])
            shopname = re.sub(r'</font>', "", shopname)
            shopname = re.sub(r'  ', "", shopname)  # 替换&nbsp;
        else:
            shopname = None
        return shopname

    def getshopprice(self, shop):
        """
        :return:商品价格
        """
        pattern = r'<div class="p-price">.*?<i>(.*?)</i></strong>'
        pprice = re.findall(pattern, shop, re.S)
        if pprice:
            shopprice = "￥ " + pprice[0]
        else:
            shopprice = None
        return shopprice

    def getshopseller(self, shop):
        """
        :return:商品卖家
        """
        pattern = r'<div class="p-shop".*? data-shopid="(.*?)">\n'

        pseller = re.findall(pattern, shop, re.S)
        if pseller:
            shopseller = pseller[0]
        else:
            shopseller = "京东自营"
        return shopseller

    def getshopcomment(self, shop):
        """
        :return:商品评论
        """
        pattern = r'<a id="J_comment_%s" target="_blank" href="(.*?)".*?>(.*?)</a>' % (shop[0])
        pcomment = re.findall(pattern, shop[1], re.S)
        if pcomment:
            href, shopcomment = pcomment[0]
        else:
            href, shopcomment = None, None
        return shopcomment

    def getpagecontent(self, response, page=1):
        """
        @返回首页的所有连接地址
        :param crawler:爬虫对象
        :return:网页中的其他文章地址
        """
        content = self.encodingdetector(response.read())
        shoppat = r'<li data-sku="(.*?)" class="gl-item">.*?<div class="gl-i-wrap">(.*?)</div>\n</li>'
        shops = re.findall(shoppat, content, re.S)
        if shops:
            print("第%d页找到商品信息%d条" % (page, len(shops)))
            for shop in shops:
                name = self.getshopname(shop[1])
                href = r"https://item.jd.com/%s.html" % (shop[0])
                price = self.getshopprice(shop[1])
                seller = self.getshopseller(shop[1])
                commentcount = self.getshopcomment(shop)
                commenthref = href + "#comment"
                self.shoplist.append([shop[0], name, href, price, seller, commentcount, commenthref])
        else:
            print("第%d页未找到商品信息" % page)

    def getfield(self, pattern, content):
        data = re.findall(pattern, content, re.S)
        if data:
            return data[0]
        else:
            return "None"

    def getpagecomment(self, response, infodic):
        """
        @返回所有评论
        """
        content = self.encodingdetector(response.read())
        commentpat = r'"content":"(.*?)","creationTime":"(.*?)"'
        comments = re.findall(commentpat, content, re.S)
        commentlist = []
        for icomment in comments[::2]:  # 评论有两个节点，选取第一个
            comment = re.sub(r'<div.*?</div>', "", icomment[0])
            comment = "[时间：%s] 评价：%s" % (icomment[1], comment)
            commentlist.append(comment)
            commentlist.append("--" * len(comment))

        if "好评度" not in infodic:
            infodic["好评度"] = self.getfield(r'"goodRateShow":(.*?),', content)
        if "商品名称" not in infodic:
            infodic["商品名称"] = self.getfield(r'"referenceName":"(.*?)",', content)
        if "晒图" not in infodic:
            infodic["晒图"] = self.getfield(r'"imageListCount":(.*?),', content)
        if "追评" not in infodic:
            infodic["追评"] = self.getfield(r'"afterCountStr":"(.*?)",', content)
        if "好评" not in infodic:
            infodic["好评"] = self.getfield(r'"goodCountStr":"(.*?)",', content)
        if "中评" not in infodic:
            infodic["中评"] = self.getfield(r'"generalCountStr":"(.*?)",', content)
        if "差评" not in infodic:
            infodic["差评"] = self.getfield(r'"poorCountStr":"(.*?)",', content)
        if "平均分" not in infodic:
            infodic["平均分"] = self.getfield(r'"averageScore":(.*?),', content)

        return infodic, commentlist

    def savecomment(self, shop, filepath):
        """
        @按时间戳存储评论
        """
        try:
            datalist = []
            infodic = {"商品ID": shop[0]}
            for i in range(3):
                url = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv235643&productId=%s&score=0&sortType=5&page=%d&pageSize=10" % (
                shop[0], i)
                response = self.checkwebsite(url)
                if response:
                    infodic, commentlist = self.getpagecomment(response, infodic)
                    datalist.extend(commentlist)
            if datalist:
                with open(filepath, "w", errors="ignore") as f:
                    f.write("商品ID:【%s】, 商品名称：%s\n" % (infodic.get("商品ID", None), infodic.get("商品名称", None)))
                    f.write("商品好评度：%s%%, 平均分：%s\n" % (infodic.get("好评度", None), infodic.get("平均分", None)))
                    f.write("晒图：%s, 追评：%s, 好评：%s, 中评：%s, 差评：%s\n" % (infodic.get("晒图", None),
                                                                     infodic.get("追评", None),
                                                                     infodic.get("好评", None),
                                                                     infodic.get("中评", None),
                                                                     infodic.get("差评", None)))
                    f.write("**" * len(infodic.get("商品ID", None) + infodic.get("商品名称", None)))
                    f.write("\n")
                    f.write("\n".join(datalist))
                self.commentcnt += 1
            else:
                self.logger.error("商品ID：%s, 商品没有找到评论。" % shop[0])
        except Exception as ex:
            self.logger.exception(str(ex))
        finally:
            urllib.request.urlcleanup()

    def save(self):
        """
        @按时间戳存储文件
        """
        dirname = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        dirpath = os.path.join(self.workdir, "JD_goods_%s" % dirname)
        os.mkdir(dirpath)
        filename = os.path.join(dirpath, "shoplist.csv")
        commentpath = os.path.join(dirpath, "comment")
        os.mkdir(commentpath)
        with open(filename, 'w', newline='', errors="ignore") as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([u"商品ID", u"商品名称", u"商品链接", u'商品价格',
                                 u"商品出售方", u"商品评论数", u"商品评论地址"])
            idx = 0
            for shop in self.shoplist:
                idx += 1
                self.savecomment(shop, os.path.join(commentpath, "%d.%s.txt" % (idx, shop[0])))  # 处理评论
                spamwriter.writerow(shop)

    def start(self, maxpage=1):
        """
        @启动爬虫
        :param maxpage:爬取最大页数
        """
        keyword = "鼠标"
        keyword = urllib.request.quote(keyword)
        for i in range(maxpage):
            url = "https://search.jd.com/Search?keyword=%s&enc=utf-8&page=%d" % (keyword, i + 1)
            response = self.checkwebsite(url)
            if response:
                try:
                    self.getpagecontent(response, i + 1)
                except Exception as ex:
                    self.logger.exception(str(ex))
                finally:
                    urllib.request.urlcleanup()
        if self.shoplist:
            self.save()
        self.logger.info("评论文件：%s" % (self.commentcnt))
        self.logger.info("End...")


if __name__ == "__main__":
    webcrawler = JdInfo()
    starttime = time.time()
    webcrawler.start(40)
    print('耗时%.2f秒' % (time.time() - starttime))

