#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from pyspark import SparkContext,SparkConf
import pymysql


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

    #公司性质-学历需求人数
    industry_edu_zpnum=data.map(lambda line: ((line[18],line[11]),int(line[9])))
    industry_edu_numbers=industry_edu_zpnum.reduceByKey(lambda x,y: x+y)
    industry_edu_counts=industry_edu_numbers.collect()


    for line in industry_edu_counts:
        cursor.execute('insert into industry_edu_counts(industry,edu,numbers) values(%s,%s,%s)',(line[0][0],line[0][1],line[1]))
        con.commit()


if __name__ == '__main__':
    main()