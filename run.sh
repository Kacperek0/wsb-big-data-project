#!/bin/bash
# assumptions:
#   * current directory of local file system of the master node
#     contains this file
#   * the input directory located in the user's home directory in HDFS
#     contains two subdirectories: datasource1 and datasource4
#     with uzipped source dataset project files - dataset (1) and (4) respectively


echo " "
echo ">>>> removing leftovers from previous launches"
# delete the project directory on HDFS
if $(hadoop fs -test -d /project) ; then hadoop fs -rm -f -r /project; fi
# remove the local output directory containing the final result of the project (6)
if $(test -d results/) ; then rm -rf results/; fi
# remove local csv files
if $(test -d *.csv) ; then rm *.csv; fi


echo " "
echo ">>>> copying scripts, files and anything else that needs to be available in HDFS to launch this script"
gsutil cp gs://dataproc-poc-ks/project/*.csv .

hadoop fs -mkdir /project

hadoop fs -copyFromLocal *.csv /project

cd mapreduce/

echo " "
echo ">>>> launching the MapReduce job - processing (2)"
mapred streaming -files mapper.py,reduce.py \
-mapper mapper.py \
-reducer reduce.py \
-combiner reduce.py \
-input /project/NYPD_Motor_Vehicle_Collisions.csv \
-output /project/output

echo " "
echo ">>>> launching the Hive/Pig script - processing (5)"
cd ..

hive -f hive/process_data.hql

echo " "
echo ">>>> getting the final result (6) from HDFS to the local file system"
mkdir results
hadoop fs -copyToLocal /project/hive/* results/

echo " "
echo " "
echo " "
echo " "
echo ">>>> presenting the obtained the final result (6)"
cat results/*
