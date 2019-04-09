#!/bin/bash
mkdir ~/data


spark-submit \
    --master local[2] \
    AverageRatingPerGenre.py \
    --input file:///home/hadoop/data/ \
    --output file:///home/hadoop/out/
	 

    
