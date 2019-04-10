#!/bin/bash
mkdir ~/data


spark-submit \
    --master local[2] \
    Top10Count.py \
    --input file:///home/hadoop/5349_a1/5349_a1/workload2/lab_commons/a1_data/ \
    --output file:///home/hadoop/out/
	 

    
