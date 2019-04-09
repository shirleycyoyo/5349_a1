import csv

def extractRating(record):

    try:
        video_id, trending_date, category, likes, dislikes, country = record.split(",")
        video_id = float(video_id)
        trending_date = float(trending_date)
        category = float(category)
        likes = float(likes)
        dislikes = float(dislikes)
        country = float(country)
        return (video_id, trending_date, category, likes, dislikes, country)
    except:
        return ()
