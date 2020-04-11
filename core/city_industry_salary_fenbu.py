#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from pyspark import SparkContext,SparkConf
import numpy as np



def main():
    master='spark://master:7077'
    conf=SparkConf().setAppName("test1").setMaster(master)
    sc=SparkContext(conf=conf)
    file_dir="hdfs:///input/data.txt"
    words=sc.textFile(file_dir)
    data=words.map(lambda line:line.split(","))


    #城市-行业-薪酬分布
    city_industry_salary_data=data.map(lambda line: ((line[1],line[18]),line[6]))
    city_industry_salary_reduce=city_industry_salary_data.reduceByKey(lambda x,y: ','.join([x,y]))
    city_industry_salary=city_industry_salary_reduce.collect()
    #print city_industry_slary


    for line in city_industry_salary:
        salary=line[1].split(',')
        salary=map(lambda x: float(x),salary)
        #print salary

        onep=str(np.percentile(salary,10))
        threep=str(np.percentile(salary,30))
        fivep=str(np.percentile(salary,50))
        sevenp=str(np.percentile(salary,70))
        ninep=str(np.percentile(salary,90))
        cursor.execute('insert into city_industry_salary_fenbu(city,industry,onep,threep,fivep,sevenp,ninep) values(%s,%s,%s,%s,%s,%s,%s)',(line[0][0],line[0][1],onep,threep,fivep,sevenp,ninep))
        con.commit()

    #城市-薪酬分布
    city_all_salary_data=data.map(lambda line: (line[1],line[6]))
    city_all_salary_reduce=city_all_salary_data.reduceByKey(lambda x,y: ','.join([x,y]))
    city_all_salary=city_all_salary_reduce.collect()

    for line in city_all_salary:
        salary=line[1].split(',')
        salary=map(lambda x: float(x),salary)
        #print salary

        onep=str(np.percentile(salary,10))
        threep=str(np.percentile(salary,30))
        fivep=str(np.percentile(salary,50))
        sevenp=str(np.percentile(salary,70))
        ninep=str(np.percentile(salary,90))
        cursor.execute('insert into city_industry_salary_fenbu(city,industry,onep,threep,fivep,sevenp,ninep) values(%s,%s,%s,%s,%s,%s,%s)',(line[0],"全部行业",onep,threep,fivep,sevenp,ninep))
        con.commit()

    #行业-薪酬分布
    all_industry_salary_data=data.map(lambda line: (line[18],line[6]))
    all_industry_salary_reduce=all_industry_salary_data.reduceByKey(lambda x,y: ','.join([x,y]))
    all_industry_salary=all_industry_salary_reduce.collect()

    for line in all_industry_salary:
        salary=line[1].split(',')
        salary=map(lambda x: float(x),salary)
        #print salary

        onep=str(np.percentile(salary,10))
        threep=str(np.percentile(salary,30))
        fivep=str(np.percentile(salary,50))
        sevenp=str(np.percentile(salary,70))
        ninep=str(np.percentile(salary,90))
        cursor.execute('insert into city_industry_salary_fenbu(city,industry,onep,threep,fivep,sevenp,ninep) values(%s,%s,%s,%s,%s,%s,%s)',("全国",line[0],onep,threep,fivep,sevenp,ninep))
        con.commit()



if __name__ == '__main__':
    main()