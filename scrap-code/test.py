from pyspark.sql import SparkSession
from pyspark import SparkContext
sc = SparkContext()
spark = SparkSession(sc)

#df = spark.read.format("json").load("../data/flight-data/json/2015-summary.json")
#df.printSchema()
df = spark.read.format("json").load("../data/flight-data/json/2015-summary.json")
df.