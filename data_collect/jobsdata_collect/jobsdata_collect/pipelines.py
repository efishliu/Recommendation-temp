# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
from scrapy.crawler import Settings as settings
from jobsdata_collect.items import Posts
import string


class JobsdataCollectPipeline(object):
    
    def __init__(self):
        
        dbargs=dict(
            host='127.0.0.1',
            db='zhaopin',
            user='root',
            passwd='liugang666',
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        self.dbpool=adbapi.ConnectionPool('MySQLdb',**dbargs)

    def process_item(self, item, spider):
        res = self.dbpool.runInteraction(self.insert_into_table,item)
        return item
        
    def insert_into_table(self,conn,item):
        conn.execute('INSERT INTO collect2(workcity,job_name,job_inwhichcompany,min_salary,max_salary,job_category,workplace,zhaopin_numbers,\
        job_welfare,education_background,min_workexperience,job_form,job_releasetime,company_name,company_form,\
        company_industry,company_scale,company_web,company_address,data_addtime,data_sourceweb,job_require,company_introduce,salary)\
         VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'\
         ,(item['workcity'],item['job_name'],item['job_inwhichcompany'],item['min_salary'],item['max_salary'],item['job_category'],item['workplace'],\
         item['zhaopin_numbers'],item['job_welfare'],item['education_background'],item['min_workexperience'],\
         item['job_form'],item['job_releasetime'],item['company_name'],item['company_form'],item['company_industry'],item['company_scale'],\
         item['company_web'],item['company_address'],item['data_addtime'],item['data_sourceweb'],item['job_require'],item['company_introduce'],item['salary']))