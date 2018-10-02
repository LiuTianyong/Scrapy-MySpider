# -*- coding: utf-8 -*-

# Scrapy settings for DgSpider project

# 图片储存
IMAGES_STORE = 'D:\\pics\\jfss\\'

# 爬取域名
DOMAIN = 'toutiao.com'

# 图片域名前缀
DOMAIN_HTTP = "http:"

# 随机发帖用户
CREATE_POST_USER = '37619,18441390,18441391,18441392,18441393,18441394,18441395,18441396,18441397,18441398,18441399,'\
                   '18441400,18441401,18441402,18441403,18441404, 18441405,18441406,18441407,18441408,18441409,' \
                   '18441410,18441411,18441412,18441413,18441414,18441415,18441416,18441417,18441418,18441419,' \
                   '18441420,18441421,18441422,18441423,18441424,18441425,18441426,18441427,18441428,18441429,' \
                   '18441430,18441431,18441432,18441433,18441434,18441435,18441436,18441437,18441438,18441439,' \
                   '18441440,18441441,18441442,18441443,18441444,18441445,18441446,18441447,18441448,18441449,' \
                   '18441450,18441451,18441452,18441453,18441454,18441455,18441456,18441457,18441458,18441460,' \
                   '18441461,18441462,18441463,18441464,18441465,18441466,18441467,18441468,18441469,18441470,' \
                   '18441471,18441472,18441473,18441474,18441475,18441476,18441477,18441478,18441479,18441481,' \
                   '18441482,18441483,18441484,18441485,18441486,18441487,18441488,18441489,18441490'

# 爬虫名
SPIDER_NAME = 'DgContentSpider_PhantomJS'

# 文章URL爬取规则XPATH
POST_TITLE_XPATH = '//h1[@class="article-title"]'
POST_CONTENT_XPATH = '//div[@class="article-content"]'

