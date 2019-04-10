import csv

def extractRating(record):
    try:
        video_id, trending_date, category_id,category,publish_time,views,likes,dislikes,comment_count,ratings_disabled,video_error_or_removed,country = record.split(",")
        return (video_id, country), (category, likes, dislikes)
    except:
        return ()

def devideData(list):
    video_id = list[0][0]
    
    country = list[0][1]
    category = list[1][0][0]
    count = (int(list[1][1][2])-int(list[1][0][2]))-(int(list[1][1][1])-int(list[1][0][1]))
    return (video_id,(count, category,country))

def getResult(value_pair):
    k,v = key_value_pair
    result = "%s,%s,%s,%s" % (k,v[0],v[1],v[2])
    return result

