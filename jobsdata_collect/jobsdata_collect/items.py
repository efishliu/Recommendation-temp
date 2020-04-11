# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsdataCollectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Posts(scrapy.Item):
    #企业信息
    company_name=scrapy.Field()
    company_form=scrapy.Field()#公司性质，eg国企
    company_industry=scrapy.Field()#公司涉及行业
    company_scale=scrapy.Field()#公司规模
    company_introduce=scrapy.Field()
    company_web=scrapy.Field()
    company_address=scrapy.Field()

    
    #职位信息
    #job_trade=scrapy.Field()#职位行业（大类）1
    workcity=scrapy.Field()
    job_name=scrapy.Field()
    job_welfare=scrapy.Field()
    job_inwhichcompany=scrapy.Field()
    job_category=scrapy.Field()#职位行业细分
    min_salary=scrapy.Field()
    max_salary=scrapy.Field()
    workplace=scrapy.Field()
    job_releasetime=scrapy.Field()
    education_background=scrapy.Field()
    zhaopin_numbers=scrapy.Field()
    min_workexperience=scrapy.Field()
    job_form=scrapy.Field()#工作性质，eg全职
    job_require=scrapy.Field()
    data_addtime=scrapy.Field()
    data_sourceweb=scrapy.Field()
    salary=scrapy.Field()

    '''
    gender_require=scrapy.Field()
    min_age=scrapy.Field()
    max_age=scrapy.Field()
    language_require=scrapy.Field()
    max_workexperience=scrapy.Field()
    '''