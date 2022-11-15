#pip install pytube3
from pytube import YouTube
from pytube import Playlist


def Download_Video(video_link ,maxres=None):
    yt = YouTube(video_link)
    stream=yt.streams.first()
    stream.download()



def DownloadChannel(channel_link,maxres=None):
    
    playlist = Playlist(channel_link)
    all_videoes=playlist.video_urls
    for i in all_videoes:
        Download_Video(i)
    #playlist.download_all()
    

#main Function Start
def main():
    DownloadChannel(channel_link="https://www.youtube.com/watch?v=B7Twzd75964&list=PLCFjzvB7O_HLROmwmh3WFGbvvikWKBK6f")

if __name__=="__main__":
    main()
#main Function End