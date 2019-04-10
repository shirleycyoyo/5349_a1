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
    parser.add_argument("--input", help="the input path",default='/')
    parser.add_argument("--output", help="the output path", default='alltryspark') 
    args = parser.parse_args()
    input_path = args.input
    output_path = args.output
    s = sc.textFile(input_path + "AllVideos_short.csv")

    parts = s.filter(lambda x: 'video_id' not in x)
    
    collectParts = parts.map(extractRating)
    data = collectParts.groupByKey().mapValues(tuple)

    
    data_remove = data.filter(lambda y: len(y[1])>1)

    data_count = data_remove.map(devideData)
    print(data_count.collect())

    ranking_list = data_count.sortBy(lambda y: (1-y[1]))
    final_result = ranking_list.take(10)
    
    final_result.saveAsTextFile(output_path)


    sc.stop()
    
    
