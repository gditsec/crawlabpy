import hashlib, os, requests, time
from datetime import date
from crawlab import save_item
from crawlabpy.utils import MEDIA_CONTENT_TYPE, notify_target, save_file

# os.environ['CRAWLAB_TARGET_HOST'] = ''
# os.environ['CRAWLAB_TARGET_PORT'] = ''
# os.environ['CRAWLAB_TARGET_USERNAME'] = ''
# os.environ['CRAWLAB_TARGET_PASSWORD'] = ''
# os.environ['CRAWLAB_TARGET_PATH'] = ''
# os.environ['CRAWLAB_TARGET_NOTIFY'] = ''
# os.environ['CRAWLAB_DATA_SOURCE'] = ''

os.environ['CRAWLAB_TARGET_HOST'] = ''
os.environ['CRAWLAB_TARGET_PORT'] = ''
os.environ['CRAWLAB_TARGET_USERNAME'] = ''
os.environ['CRAWLAB_TARGET_PASSWORD'] = ''
os.environ['CRAWLAB_TARGET_PATH'] = ''
os.environ['CRAWLAB_TARGET_NOTIFY'] = ''
os.environ['CRAWLAB_DATA_SOURCE'] = ''

if __name__ == '__main__':
    img_url_list = [
        'http://www.gditsec.org.cn/images/pic_hbs1.jpg',
        'http://www.gditsec.org.cn/images/pic_hbs3.jpg',
        'http://www.gditsec.org.cn/images/pic_hbs2.jpg'
    ]
    img_name_list = []

    for img_url in img_url_list:
        img = requests.get(url=img_url).content
        img_name = hashlib.md5(img).hexdigest() + '.jpg'
        img_name_list.append(img_name)
        save_file(img_name, img)

    down_date = date.strftime(date.fromtimestamp(time.time()), '%Y-%m-%d %H:%M:%S')
    
    result = {
        'body': 'test body',
        'body_cn': '',
        'body_en': 'test body',
        'covering': img_name_list,
        'downdate': down_date,  # 爬虫时间
        'id': '123456',
        'languageid': '10001',
        'languagename': '英语',
        'pagedate': down_date,
        'partid': '3',  # 板块号
        'partname': 'test_part_name',  # 板块名
        'resource': img_name_list,
        'sectionid': '',
        'sectionname': '缅甸',
        'siteid': '153',
        'sitename': '缅甸新闻网',
        'title': 'test title',
        'title_cn': '',
        'title_en': 'test title',
        'url': 'http://example.com/news/1.html',
        'viewcount': '',
        'writer': ''
    }
    save_item(result)
    notify_target(MEDIA_CONTENT_TYPE, result, img_name_list)

