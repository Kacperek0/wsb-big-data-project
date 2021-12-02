#!/bin/bash

cat NYPD_Motor_Vehicle_Collisions.csv | python3 mapreduce/mapper.py | sort | python3 mapreduce/combiner.py > test.txt
