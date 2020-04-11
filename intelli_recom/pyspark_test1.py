# -*- coding: utf-8 -*-
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
from pyspark import SparkContext,SparkConf


def main():
    master='spark://master:7077'
    conf=SparkConf().setAppName("test1").setMaster(master)
    sc=SparkContext(conf=conf)
    file_dir="hdfs:///jobsdata/part-m-00000"
    words=sc.textFile(file_dir)
    #a=words.first()
    #a=words.map(lambda x:x.split(',')).take(1)
    #data=words.map(lambda x:x.split(','))
    #a=data.take(1)
    city_industry_number=words.map(lambda x:((x[2],x[36]),x[18])).reduceByKey(lambda x,y:x+y)
    a=city_industry_number.collect()
    print a
    #idcount=data.map(lambda x:x[0]).count()
    #idcount=words.count()
    #print idcount
    
    



if __name__ == '__main__':
    main()