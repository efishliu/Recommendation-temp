# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from jobsdata_collect.items import Posts
import datetime
import string 
import re 

class Collect1Spider(scrapy.Spider):
    name = 'collect'
    allowed_domains = ['jobs.zhaopin.com']
    start_urls = ['http://jobs.zhaopin.com/']

    def parse(self, response):
        #
        for inlist in response.css('div.listcon a::attr(href)').extract():    
            yield response.follow(inlist,self.parse_href)
            
    def parse_href(self,response):
        for nextlist in response.css('div.searchlist_page span.search_page_next a::attr(href)').extract():
            yield response.follow(nextlist,self.parse_href)
        #
        for wolist in response.css('div.main-left.main_current_items div.details_container span.post a::attr(href)').extract():
            yield response.follow(wolist,self.parse_message)


    #parse 具体信息
    def parse_message(self,response):
        item=Posts()
        item['workcity']=''.join(response.css('div.terminalpage-left ul.terminal-ul.clearfix li')[1].css('strong a::text').extract_first()).replace('\n','').replace('\r','').replace('\t','').replace(',',' ').strip('\n')
        item['company_name']=''.join(response.css('div.company-box p.company-name-t a::text').extract_first().strip()).replace('\n','').replace('\r','').replace('\t','').replace(',',' ').strip('\n')
        item['company_form']=''.join(response.css('ul.terminal-ul.clearfix.terminal-company.mt20 li strong::text').extract()[1].strip()).replace('\n','').replace('\r','').replace('\t','').replace(',',' ').strip('\n')
        item['company_industry']= ''.join(response.css('ul.terminal-ul.clearfix.terminal-company.mt20 li strong a::text').extract()[0].strip()).replace('\n','').replace('\r','').replace('\t','').replace(',',' ').strip('\n')
        item['company_scale']= ''.join(response.css('ul.terminal-ul.clearfix.terminal-company.mt20 li strong::text').extract()[0].strip()).replace('\n','').replace('\r','').replace('\t','').replace(',',' ').strip('\n')
        item['company_web']=''.join(response.css('div.company-box p.company-name-t a::attr(href)').extract_first()).replace('\n','').replace('\r','').replace('\t','').replace(',',' ').strip('\n')
        item['company_address']=''.join(response.css('ul.terminal-ul.clearfix.terminal-company.mt20 li strong::text').extract()[-1].strip()).replace('\n','').replace('\r','').replace('\t','').replace(',',' ').strip('\n')
        item['job_name']=''.join(response.css('div.fixed-inner-box  h1::text').extract()).replace('\n','').replace('\r','').replace('\t','').replace(',',' ').strip('\n')
        item['job_inwhichcompany']=''.join(response.css('div.fixed-inner-box  h2 a::text').extract()).replace('\n','').replace('\r','').replace('\t','').replace(',',' ').strip('\n')
        item['job_welfare']=''.join(response.css('div.fixed-inner-box div.welfare-tab-box span::text').extract()).replace('\n','').replace('\r','').replace('\t','').replace(',',' ').strip('\n')
        try:
            s=''.join(response.css('div.terminalpage-left ul.terminal-ul.clearfix li strong::text').extract()[0]).replace('\n','').replace('\r','').replace('\t','').replace(',',' ').strip('\n')
            item['min_salary']=re.findall('(\d+)',s)[0]
            item['max_salary']=re.findall('(\d+)',s)[1]
            item['salary']=str((float(item['min_salary'])+float(item['max_salary']))/2)

        except:
            pass
        item['job_releasetime']=''.join(response.css('span#span4freshdate::text').extract()).replace('\n','').replace('\r','').replace('\t','').replace(',',' ').strip('\n')
        if item['job_releasetime']=='0002-01-01 00:00:00':
            item['job_releasetime']=datetime.datetime.now().strftime('%Y-%m-%d')
        item['job_form']=''.join(response.css('div.terminalpage-left ul.terminal-ul.clearfix li strong::text').extract()[-4]).replace('\n','').replace('\r','').replace('\t','').replace(',',' ').strip('\n') #工作性质,全职
        item['min_workexperience']=''.join(response.css('div.terminalpage-left ul.terminal-ul.clearfix li strong::text').extract()[-3]).replace('\n','').replace('\r','').replace('\t','').replace(',',' ').strip('\n')
        item['education_background']=''.join(response.css('div.terminalpage-left ul.terminal-ul.clearfix li strong::text').extract()[-2]).replace('\n','').replace('\r','').replace('\t','').replace(',',' ').strip('\n')
        p=''.join(response.css('div.terminalpage-left ul.terminal-ul.clearfix li strong::text').extract()[-1]).replace('\n','').replace('\r','').replace('\t','').replace(',',' ').strip('\n')
        item['zhaopin_numbers']=re.findall('(\d+)',p)[0]
        item['job_category']=''.join(response.css('div.terminalpage-left ul.terminal-ul.clearfix li strong a::text').extract()[-1]).replace('\n','').replace('\r','').replace('\t','').replace(',',' ').strip('\n') #职位类别
        item['workplace']=''.join(response.css('div.tab-cont-box div.tab-inner-cont h2::text').extract()[0].strip()).replace('\n','').replace('\r','').replace('\t','').replace(',',' ').strip('\n')
        item['data_addtime']=datetime.datetime.now().strftime('%Y-%m-%d')

        introduce=response.css('div.terminalpage-main.clearfix div.tab-inner-cont')
        a1=''.join(introduce[1].css('p::text').extract()).strip()
        a2=''.join(introduce[1].css('span::text').extract()).strip()
        a3=''.join(introduce[1].css('div::text').extract()).strip()
        a=(a1+a2+a3).replace('\n','').replace('\r','').replace('\t','').replace(',',' ').strip('\n')
        b1=''.join(introduce[0].css('p::text').extract()).strip()
        b2=''.join(introduce[0].css('span::text').extract()).strip()
        b3=''.join(introduce[0].css('div::text').extract()).strip()
        b=(b1+b2+b3).replace('\n','').replace('\r','').replace('\t','').replace(',',' ').strip('\n')
        item['company_introduce']=a
        item['job_require']= b

        item['data_sourceweb']=''.join(response.url)
        yield item
