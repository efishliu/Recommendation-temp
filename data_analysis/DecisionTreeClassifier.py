from pyspark.ml.linalg import Vectors from pyspark.ml.feature import StringIndexer
df = spark.createDataFrame([(1.0, Vectors.dense(1.0)),(0.0, Vectors.sparse(1, [], []))], ["label", "features"])
stringIndexer = StringIndexer(inputCol="label", outputCol="indexed")
si_model = stringIndexer.fit(df)
td = si_model.transform(df)
dt = DecisionTreeClassifier(maxDepth=2, labelCol="indexed")
model = dt.fit(td)
model.numNodes
#3
 model.depth
#1
model.featureImportances
#SparseVector(1, {0: 1.0})
 model.numFeatures
#1
model.numClasses
#2
print(model.toDebugString)
#DecisionTreeClassificationModel (uid=...) of depth 1 with 3 nodes...
test0 = spark.createDataFrame([(Vectors.dense(-1.0),)], ["features"])
result = model.transform(test0).head()
result.prediction
#0.0
result.probability
#DenseVector([1.0, 0.0])
result.rawPrediction
#DenseVector([1.0, 0.0])
test1 = spark.createDataFrame([(Vectors.sparse(1, [0], [1.0]),)], ["features"])
model.transform(test1).head().prediction
#1.0
dtc_path = temp_path + "/dtc"
dt.save(dtc_path)
dt2 = DecisionTreeClassifier.load(dtc_path)
dt2.getMaxDepth()
#2
model_path = temp_path + "/dtc_model"
model.save(model_path)
model2 = DecisionTreeClassificationModel.load(model_path)
model.featureImportances == model2.featureImportances
#True