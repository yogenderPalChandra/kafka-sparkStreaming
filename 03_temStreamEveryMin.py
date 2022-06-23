

import os


import pyspark.sql.functions as F

from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, IntegerType, \
    StringType, FloatType, TimestampType
from pyspark.sql.functions import col



def main():


    spark = SparkSession \
        .builder \
        .appName("kafka-streaming-sales-console") \
        .master("local[*]") \
        .getOrCreate()

    df_TH = read_from_kafka(spark)

    calculate_average_tem(df_TH)


def read_from_kafka(spark):
    '''This read the stream with readStream and finally later prints to the console
    '''

    df_T = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "spark_topic_tem") \
        .option("startingOffsets", "earliest") \
        .load()

    return df_T


def calculate_average_tem(df_T):
    ''' This function reads the data from the topic still no average calculated,
    But calculates the strem read data (i.e. spark streaming) Tavg. 

    '''
    
    
    schema = StructType([StructField("id", IntegerType(), False),StructField("dateTime", StringType(), False),\
	StructField("Tamb", FloatType(), False),StructField("TtopTestTankHPCir", FloatType(), False),StructField("TbottomTestTankHpCir", StringType(), False),\
	StructField("TtopSourceTank",  FloatType(), False), StructField("TloadTankMix",  FloatType(), False), StructField("TTopTestTankLoadCir",  FloatType(), False), \
        StructField("TloadMix",  FloatType(), False), StructField("TbottomSourceTank",  FloatType(), False),  StructField("TbottomTestTankLoadCir",  FloatType(), False), \
        StructField("T0",  FloatType(), False),StructField("T1",  FloatType(), False), StructField("T2",  FloatType(), False), StructField("T3",  FloatType(), False), \
        StructField("T4",  FloatType(), False), StructField("T5",  FloatType(), False), StructField("T6",  FloatType(), False), StructField("T7",  FloatType(), False), \
        StructField("T8",  FloatType(), False), StructField("T9",  FloatType(), False), StructField("flowHP",  FloatType(), False), StructField("flowLoad",  FloatType(), False), \
        StructField("Load_kW",  FloatType(), False), StructField("Heat_Capacity_kW",  FloatType(), False)])

    T = [col('T0'), col('T1'), col('T2'), col('T3'), col('T4'),col('T5'),col('T6'),col('T7'),col('T8'),col('T9')]
    averageFunc = sum(x for x in T)/len(T)


    df_T = df_T \
        .selectExpr("CAST(value AS STRING)") \
        .select(F.from_json("value", schema=schema).alias("data")) \
        .select("data.*") \
        .withColumn('Tem(Avg)', averageFunc) \
        .coalesce(1) \
        .writeStream \
        .queryName("streaming_to_console") \
        .trigger(processingTime="1 minute") \
        .outputMode("append") \
        .format("console") \
        .option("numRows", 25) \
        .option("truncate", False) \
        .start()

    df_T.awaitTermination()



if __name__ == "__main__":
    main()
