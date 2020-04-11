import numpy
from numpy import allclose
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import StringIndexer
df = spark.createDataFrame([
     (1.0, Vectors.dense(1.0)),
    (0.0, Vectors.sparse(1, [], []))], ["label", "features"])
stringIndexer = StringIndexer(inputCol="label", outputCol="indexed")
si_model = stringIndexer.fit(df)
td = si_model.transform(df)
rf = RandomForestClassifier(numTrees=3, maxDepth=2, labelCol="indexed", seed=42)
model = rf.fit(td)
model.featureImportances

#SparseVector(1, {0: 1.0})
allclose(model.treeWeights, [1.0, 1.0, 1.0])
#True
test0 = spark.createDataFrame([(Vectors.dense(-1.0),)], ["features"])
result = model.transform(test0).head()
result.prediction
#0.0
numpy.argmax(result.probability)
#0
numpy.argmax(result.rawPrediction)
#0
test1 = spark.createDataFrame([(Vectors.sparse(1, [0], [1.0]),)], ["features"])
model.transform(test1).head().prediction
#1.0
model.trees
#[DecisionTreeClassificationModel (uid=...) of depth..., DecisionTreeClassificationModel...]
rfc_path = temp_path + "/rfc"
rf.save(rfc_path)
rf2 = RandomForestClassifier.load(rfc_path)
 rf2.getNumTrees()
#3
model_path = temp_path + "/rfc_model"
model.save(model_path)
model2 = RandomForestClassificationModel.load(model_path)
model.featureImportances == model2.featureImportances
#True