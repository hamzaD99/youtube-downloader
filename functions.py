import os
from pytube import YouTube
from pytube import Playlist
import shutil

def create_folder(path):
    pathToCheck = "./Output/{}".format(path)
    if(not os.path.isdir(pathToCheck)):
        os.makedirs(pathToCheck)
        print("[create_folder] New folder is created!")

def handel_url(url):
    try:
        result = YouTube(url)
        return result
    except Exception as e:
        print("[handel_url] Something went wrong!")
        print(str(e))

def handel_video(video,format,path):
    try:
        title = video.title
        print("[handel_video] '{}' downloading".format(title))
        oldPath = ''
        if(format == "audio"):
            oldPath = video.streams.get_audio_only().download()
        else:
            oldPath = video.streams.get_highest_resolution().download()
        title = oldPath.split("\\")[-1]
        newPath = "./Output/{}/{}".format(path,title)
        shutil.move(oldPath,newPath)
        print("[handel_video] '{}' downloaded and moved to the path".format(title))
    except Exception as e:
        print("[handel_video] Something went wrong!")
        print(str(e))

def handel_playlist(url,format,path):
    try:
        playlist = Playlist(url)
        path = "{}/{}".format(path,playlist.title)
        create_folder(path)
        print("[handel_playlist] '{}' downloading".format(playlist.title))
        for video in playlist.videos:
            handel_video(video,format,path)
    except Exception as e:
        print("[handel_playlist] Something went wrong!")
        print(str(e))