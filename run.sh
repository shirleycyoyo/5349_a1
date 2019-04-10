#!/bin/bash
##mkdir ~/data


spark-submit \
    --master local[2] \
    Top10Count.py \
    --input $1 \
    --output $2
    
    ##--input file:///home/hadoop/5349_a1/5349_a1/workload2/lab_commons/a1_data/ \
	 

    
