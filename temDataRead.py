
import os
import pyspark.sql.functions as F
from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, IntegerType, StringType, FloatType
from pyspark.sql.window import Window


def read_csv():
    spark = SparkSession.builder.appName("kafka-seed-tem").getOrCreate()
    path = "/home/yogender/Desktop/kafka/kafkaTemfiles/csvFile_2021_01_27.csv"

    schema = StructType([StructField("Unnamed: 0", IntegerType(), False),\
        StructField("id", IntegerType(), False),StructField("dateTime", StringType(), False),\
	StructField("Tamb", FloatType(), False),StructField("TtopTestTankHPCir", FloatType(), False),StructField("TbottomTestTankHpCir", StringType(), False),\
	StructField("TtopSourceTank",  FloatType(), False), StructField("TloadTankMix",  FloatType(), False), StructField("TTopTestTankLoadCir",  FloatType(), False), \
        StructField("TloadMix",  FloatType(), False), StructField("TbottomSourceTank",  FloatType(), False),  StructField("TbottomTestTankLoadCir",  FloatType(), False), \
        StructField("T0",  FloatType(), False),StructField("T1",  FloatType(), False), StructField("T2",  FloatType(), False), StructField("T3",  FloatType(), False), \
        StructField("T4",  FloatType(), False), StructField("T5",  FloatType(), False), StructField("T6",  FloatType(), False), StructField("T7",  FloatType(), False), \
        StructField("T8",  FloatType(), False), StructField("T9",  FloatType(), False), StructField("flowHP",  FloatType(), False), StructField("flowLoad",  FloatType(), False), \
        StructField("Load_kW",  FloatType(), False), \
        StructField("Heat_Capacity_kW",  FloatType(), False)])
	

    df = spark.read.csv(path=path,schema=schema, header=True, sep=",").drop("Unnamed: 0")


    df.selectExpr("CAST(id AS STRING) AS key","to_json(struct(*)) AS value").write.format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("topic", "spark_topic_tem").save()

        
if __name__=="__main__":
    read_csv()
