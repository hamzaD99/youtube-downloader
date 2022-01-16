# Youtube-Downloader
This script is useful for anyone needs to download multiple videos or playlist from youtube, you can just provide the list of URLs and the script will download them.

# How to use it?
You need to fill `Videos.csv` file as follows:
	**1- url column:** To provide the URL for the video or the playlist.
	**2- playlist(0,1) column:** type 0 for video, 1 for playlist.
	**3- video/audio column:** type 'video' if you want the URL as video, 'audio' for audio.
	**4- path to download column:** type the path you want the file to be in after the download.
If something went wrong with one of the links, the report will file `Report.txt` will be updated.
Check the video to see a demo:
https://youtu.be/Zzoo6xWEfug

# Requierments
You must have python 3 with `pytube` library installed.
https://pytube.io/en/latest/
