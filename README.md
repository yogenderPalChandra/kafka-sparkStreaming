# Getting Started with Spark Structured Streaming and Kafka
This repo locally sets up kafka clusters, read local csv files into topic. Performs batch queries, streaming queries, and incremental queries.

Requirements: 
Local installation of Spark and Kafka
```
git clone https://github.com/yogenderPalChandra/kafka-sparkStreaming.git
```

You will be moving across many many terminals, depending upon where your kafka installation was done! Or you can set up environment variables for $SPARK_HOME
and $KAFKA_HOME, and update ~/.profile (or ~/.bashrc, for that matter) and run the scripts from anywhere

1. Read data from csv file:

```
cd <path/to/PySpark/installation>
bin/spark-submit  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1 <path/to/your/cloned/directory/temDataRead.py>

```
to check whether data is pushed to the topic:
```
cd /path/to/kafka-server
bin/kafka-console-consumer.sh \
--bootstrap-server localhost:9092 --topic spark_topic_tem --from-beginning
```

2 Read from topicand do some analysis:

in another terminal go to spark installation:
```
cd <path/to/PySpark/installation>
bin/spark-submit  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1 <path/to/your/cloned/directory/temReadFromTopic.py>
```

3 batch query:
in yet another terminal do:

```
cd <path/to/PySpark/installation>
bin/spark-submit  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1 <path/to/your/cloned/directory/03_temStreamEveryMin.py>
```

4 Streaming queries to console:
in yet another terminal do:

```
cd <path/to/PySpark/installation>
bin/spark-submit  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1 /home/yogender/Desktop/kafka/kafkaTemfiles/04_temincrementaltem.py
```
