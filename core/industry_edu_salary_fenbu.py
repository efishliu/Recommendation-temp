#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from pyspark import SparkContext,SparkConf
import pymysql
import numpy as np


def mysqlconnect():
    con=pymysql.connect(
        host='172.17.42.169',
        port=3306,
        user='root',
        passwd='liugang666',
        database='zhaopin',
        charset='utf8',
    )
    return con

def main():
    con=mysqlconnect()
    cursor=con.cursor()
    master='spark://master:7077'
    conf=SparkConf().setAppName("test1").setMaster(master)
    sc=SparkContext(conf=conf)
    file_dir="hdfs:///data/part-m-00000"
    words=sc.textFile(file_dir)
    data=words.map(lambda line:line.split(","))


    #行业-学历-薪酬分布
    industry_edu_salary_data=data.map(lambda line: ((line[18],line[11]),line[6]))
    industry_edu_salary_reduce=industry_edu_salary_data.reduceByKey(lambda x,y: ','.join([x,y]))
    industry_edu_salary=industry_edu_salary_reduce.collect()
    #print industry_edu_slary


    for line in industry_edu_salary:
        salary=line[1].split(',')
        salary=map(lambda x: float(x),salary)
        #print salary

        onep=str(np.percentile(salary,10))
        threep=str(np.percentile(salary,30))
        fivep=str(np.percentile(salary,50))
        sevenp=str(np.percentile(salary,70))
        ninep=str(np.percentile(salary,90))
        cursor.execute('insert into industry_edu_salary_fenbu(industry,edu,onep,threep,fivep,sevenp,ninep) values(%s,%s,%s,%s,%s,%s,%s)',(line[0][0],line[0][1],onep,threep,fivep,sevenp,ninep))
        con.commit()




if __name__ == '__main__':
    main()