#!/usr/bin/python3

import sys
#from operator import itemgetter, attrgetter

def read_file(file):
    for line in file:
        yield line.strip()

def main():
    file = sys.stdin
    lines = read_file(file)
    for line in lines:

        a = line.strip()
        parts = a.split(",")

        video_id = parts[0]
        categories = parts[3]
        countries = parts[11]

        print("{}\t{}\t{}".format(categories,video_id, countries))

if __name__ == "__main__":
    main()


    
