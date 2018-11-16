#!/usr/bin/python3
# Title=全书网 小说爬虫
# Date=2018-03-02

import requests


class NovelSpider:
    """全书网，小说爬虫"""
    def __init__(self):
        self.session = requests.Session()

    def get_novel(self, url):
        """下载小说"""
        # 下载小说的首页面的html
        index_html = self.download(url, encoding='gb2312')

        # 提取章节信息
        novel_chapter_infos = self.get_chapter_info(index_html)

        # 保存章节信息
        # self,save_novel(novel_chapter_infos)
        print(index_html)

    def get_chapter_info(self, index_html):



    def download(self, url, encoding):
        """下载html源码"""
        response = self.session.get(url)
        response.encoding = encoding
        html = response.text

        return html

if __name__ == '__main__':
    novel_url = 'http://www.quanshuwang.com/book/44/44683'
    spider = NovelSpider()
    spider.get_novel(novel_url)