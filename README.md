# Crawlab Python SDK

<img src="https://img.shields.io/badge/Python-3.8.10-blue">

## 基本用法
```python
from crawlabpy.utils import notify_target, save_file

img = requests.get(url=img_url).content
img_name = hashlib.md5(img).hexdigest() + '.jpg'
save_file(img_name, img)

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
save_item(result)
notify_target(result, img_name_list)
```
