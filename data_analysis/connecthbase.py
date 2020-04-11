import pyspark
spark = SparkSession.builder.master("yarn-client").appName("statistics").getOrCreate()

hbaseconf = {"hbase.zookeeper.quorum":host,"hbase.mapreduce.inputtable":inputtable}

keyConv = "org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter"

valueConv = "org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter"

hbase_rdd = spark.sparkContext.newAPIHadoopRDD(\
"org.apache.hadoop.hbase.mapreduce.TableInputFormat",\
"org.apache.hadoop.hbase.io.ImmutableBytesWritable",\
"org.apache.hadoop.hbase.client.Result",\
keyConverter=keyConv, valueConverter=valueConv, conf=hbaseconf)

hbase_rdd.count()