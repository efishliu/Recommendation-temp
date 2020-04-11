#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from pyspark import SparkContext,SparkConf



def main():
    master='spark://master:7077'
    conf=SparkConf().setAppName("data_test").setMaster(master)
    sc=SparkContext(conf=conf)
    file_dir="hdfs:///data/part-m-00000"
    words=sc.textFile(file_dir)
    data=words.map(lambda line:line.split(","))
    test=data.filter(lambda x: x[18]==unicode("计算机软件",'utf-8'))
    #require=data.map(lambda line:(line[0],' '.join(analyse.extract_tags(line[1],topK=10))))
    result=test.take(5)
    #require.saveAsTextFile("hdfs:///keywords/")

    #require_fenci=require.take(3)
    #result=require.take(35)

    #print require_fenci[1]
    print result

if __name__ == '__main__':
    main()

