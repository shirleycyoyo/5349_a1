# Calculate the average rating of each genre
# In order to run this, we use spark-submit, below is the 
# spark-submit  \
#   --master local[2] \
    #   AverageRatingPerGenre.py
#   --input input-path
#   --output outputfile

from pyspark import SparkContext
from ml_utils import *
import argparse


if __name__ == "__main__":
    sc = SparkContext(appName="Top 10 dislikes")
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="the input path",
                        default='/')
    parser.add_argument("--output", help="the output path", 
                        default='alltryspark') 
    args = parser.parse_args()
    input_path = args.input
    output_path = args.output
    
    parts = sc.textFile(input_path + "ratings.csv")
    
    collectParts = parts.map(extractRating)
    
    collectParts.saveAsTextFile(output_path)

    sc.stop()
    
    
