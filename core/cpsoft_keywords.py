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
    conf=SparkConf().setAppName("cpsoft_keywords").setMaster(master)
    sc=SparkContext(conf=conf)
    file_dir="hdfs:///data/part-m-00000"
    jieba.load_userdict("/opt/mydict.txt")
    words=sc.textFile(file_dir)
    jieba.analyse.set_stop_words('/opt/stopwords.txt')
    data=words.map(lambda line:line.split(",")).filter(lambda x: x[18]==unicode("计算机软件",'utf-8'))
    #require=data.map(lambda line:(line[0],line[15]))
    require=data.map(lambda line:(line[0],' '.join(analyse.extract_tags(line[15],topK=20))))
    #print require.take(10)
    result=require.collect()
    con=mysqlconnect()
    cursor=con.cursor()
    for line in result:
        try:
            cursor.execute('insert into keywords(id,keywords) values(%s,%s)',(str(line[0]),str(line[1])))
            con.commit()
        except:
            pass
    con.close()


if __name__ == '__main__':
    main()

