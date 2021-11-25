import hashlib
import time
import requests
from lxml import etree
from crawlab import save_item
from crawlabpy import save_file


def response(get_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'}
    resp = requests.get(url=get_url, headers=headers)
    resp.encoding = 'utf-8'
    if resp.status_code == 200:
        return etree.HTML(resp.text)
    else:
        return resp.status_code


def time_now():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def make_id(news_title, text_list):
    # 标题+正文-->>MD5-->>去重
    if news_title and text_list:  # 判断title和body都不为空
        data = news_title[0] + text_list[0]
    else:
        data = news_title[0]
    return hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()


def run():
    main_url = 'https://www.myanmarnews.net'
    international_news_url = main_url + '/category/b8de8e630faf3631'
    html = response(international_news_url)

    # xpath
    news_url_list1 = html.xpath('//*[@class="large-9 medium-8 columns left_content"]//*/h5/a/@href')
    news_url_list2 = html.xpath('//*[@class="large-9 medium-8 columns left_content"]//*/h6/a/@href')

    # url list
    news_url_list = []
    for url1 in news_url_list1:
        news_url_list.append(url1)
    for url2 in news_url_list2:
        news_url_list.append(url2)

    # requests url list
    for url in news_url_list:
        news_url = main_url + url
        print(main_url)
        html = response(news_url)
        news_title = html.xpath('//*[@class="large-12 columns"]//*[@class="title_text"]/h2/a/text()')
        text_list = html.xpath('//*[@class="large-12 columns"]//*[@class="text"]/p/text()')
        img_urls = html.xpath('//*[@class="article_image"]/img/@src')
        print(news_title)
        print(text_list)

        # 图片处理
        img_name_list = []
        if img_urls:
            for img_url in img_urls:
                # <--无需切片-->
                print("img url>>>", img_url)
                img = requests.get(url=img_url).content
                img_name = hashlib.md5(img).hexdigest() + '.jpg'
                img_name_list.append(img_name)
                img_img = {img_name: img}
                # save_item(img_img)
                save_file(img_name, img)
                # with open(img_name, "wb") as file:
                #     file.write(img)

        # 文本处理
        text = ''.join(text_list)

        if img_urls:
            image_head = ''
            for img_name_md5 in img_name_list:
                image_head += '{i_m_a_g_e|' + img_name_md5 + '}'
            body = image_head + text
        else:
            body = text

        news_id = make_id(news_title, text_list)

        down_date = time_now()
        try:
            result = {
                'body': body,
                'body_cn': '',
                'body_en': body,
                'covering': img_name_list,
                'downdate': down_date,  # 爬虫时间
                'id': news_id,
                'languageid': '10001',
                'languagename': '英语',
                'pagedate': down_date,
                'partid': '3',  # 板块号
                'partname': '对外关系,国际关系',  # 板块名
                'resource': img_name_list,
                'sectionid': '',
                'sectionname': '缅甸',
                'siteid': '153',
                'sitename': '缅甸新闻网',
                'title': news_title[0],
                'title_cn': '',
                'title_en': news_title[0],
                'url': news_url,
                'viewcount': '',
                'writer': ''
            }
            # print(result)
            save_item(result)
        except IndexError:
            continue


if __name__ == '__main__':
    run()
