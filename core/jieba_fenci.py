#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from pyspark import SparkContext,SparkConf
import jieba
from jieba import analyse
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
    master='spark://master:7077'
    conf=SparkConf().setAppName("jieba_fenci").setMaster(master)
    sc=SparkContext(conf=conf)
    file_dir="hdfs:///data/part-m-00000"
    words=sc.textFile(file_dir)
    data=words.map(lambda line:line.split(","))
    #require=data.map(lambda line: (line[0],' '.join(analyse.extract_tags(line[15],topK=20))))
    require=data.map(lambda line: ' '.join(jieba.cut(line[15])))
    require_fenci=require.take(3)
    #require_fenci=require.collect()
    #require_fenci=require.first()
    #print require_fenci
    print require_fenci[1]
    '''
    con=mysqlconnect()
    cursor=con.cursor()
    for line in require_fenci:
        #print line[0]
        #print line[1]
        cursor.execute('insert into keywords(id,keywords) values(%s,%s)',(str(line[0]),str(line[1])))
        con.commit()
    '''
if __name__ == '__main__':
    main()

