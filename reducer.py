import sys
from collections import defaultdict

def read_map_output(file):

    for lines in file:
        yield lines.strip().split("\t")

def main():
    file = sys.stdin

    current_category = ""
    video_country = {}
    category_video = {}
    current_video_id = ""
    current_video = ""
    i=0
    j=0
    k=0
    q=0
    p=0

    for categories, video_id, countries in read_map_output(file):
        
        if current_video_id != categories + video_id:
            if current_video_id !="":

                for country, count in category_video.items():
                    i=i+1
                if current_category == "":
                    j=0
                if current_category != "":
                    if current_category !='category':
                        if current_category == categories:
                            j=j+i
                            k=j
                            q=q+1
                        if current_category != categories:
                            j=j+i
                            k=j
                            q=q+1
                            p=q
                            q=0
                            j=0

                            output = current_category + ":"+ " {}".format(round(k/p,2))
                            print(output.strip())
        
            current_category = categories
            current_video = video_id

            # Reset the tag being processed and clear the owner_count dictionary for the new tag
            current_video_id = categories + video_id
            category_video = {}
            i=0

        category_video[countries] = category_video.get(countries, 0) + 1

        
    if current_video_id != "":
        output = current_video_id + "\t"
        for country, count in category_video.items():
            i=i+1
        if current_category == "":
            j=0
        if current_category != "":
            if current_category == categories:
                j=j+i
                k=j
            if current_category != categories:
                j=j+i
                k=j
                j=0
        output = current_category +":"+" {}".format(round(k/p,2))
        print(output.strip())
        i=0

if __name__ == "__main__":
    main()
        
