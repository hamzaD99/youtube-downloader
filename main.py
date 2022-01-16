from pytube import YouTube
import csv
file = open("Videos.csv","r")
csv_reader = csv.reader(file,delimiter=',')
counter = 0

for row in csv_reader:
    if(counter == 0):
        counter = 1
    else:
        print(row)

file.close()


video = YouTube('https://www.youtube.com/watch?v=cAybOj9hQe8')

#print(video.streams.get_audio_only().download())