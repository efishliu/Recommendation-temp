#coding=utf-8
from pyspark import SparkContext, SparkConf

import sys
sys.path.append('/usr/lib64/python2.6/site-packages/hbase/')
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase
from hbase.ttypes import *
transport = TSocket.TSocket('192.168.1.131', 9090)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = Hbase.Client(protocol)
transport.open()
print(client.getTableNames())


sc=SparkContext('local','each_industry_count')