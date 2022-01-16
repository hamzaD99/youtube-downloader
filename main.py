import csv
import functions
file = open("Videos.csv","r")
csv_reader = csv.reader(file,delimiter=',')
counter = 0
report_file = open("Report.txt","a")
for row in csv_reader:
    if(counter == 0):
        counter = 1
    else:
        url = row[0]
        playlist = row[1]
        format = row[2]
        path = row[3]
        functions.create_folder(path)
        if(playlist == "1"):
            functions.handel_playlist(url,format,path,report_file)
        else:
            video = functions.handel_url(url)
            functions.handel_video(video,format,path,report_file)
file.close()
report_file.close()