import requests
from lxml import etree

class Budejie_Spider(object):
    def __init__(self):
        self.start_url = 'http://www.budejie.com/'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        self.page_num = 1

    def get_html_content(self,html_str):  # 提取指定作者头像地址，作者昵称，段子内容，段子图片地址，段子点赞数
        temp_html_object = etree.HTML(html_str)
        html_content_list = temp_html_object.xpath("//div[@class='j-r-list']")
        for temp_object in html_content_list:
            for temp_son_object in temp_object.xpath('./ul/li'):
                items = {}
                items['author_image_url'] = temp_son_object.xpath('''.//img[@class='u-logo lazy']/@data-original''')
                items['author_name'] = temp_son_object.xpath(".//div[@class='u-txt']/a/text()")
                items['tittle_content'] = temp_son_object.xpath(".//div[@class='j-r-list-c-desc']/a/text()")
                items['tittle_image_url'] = temp_son_object.xpath(".//div[@class='j-r-list-c-img']//img/@data-original")
                items['num_for_nice'] = temp_son_object.xpath(".//li[@class='j-r-list-tool-l-up']/span/text()")
                print(items)


    def parse_url(self,url = 'http://www.budejie.com/'):  # 解析网址
        html_str = requests.get(url, headers=self.headers)
        print(url)
        self.page_num += 1
        next_page_url = self.start_url + str(self.page_num)
        if html_str.status_code == 200:
            self.get_html_content(html_str.content)
            return self.parse_url(next_page_url)
        else:
            print('Done')


    def run(self):
        # 获取首页地址
        # 访问地址
        html_str = self.parse_url()
        # 提取网页内容，图片地址，下一页地址
            # 访问下一页地址
            # 提取数据
        # 保存数据


if __name__ == '__main__':
    Budejie = Budejie_Spider()
    Budejie.run()