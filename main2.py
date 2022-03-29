# Downloading multiple videos

from pytube import YouTube 
  
#where to save 
SAVE_PATH = "D:\codingtest" #to_do 

#link of the video to be downloaded 
link=["https://www.youtube.com/watch?v=JfZ7KRgaDpk",
     "https://www.youtube.com/watch?v=MHPGeQD8TvI"]

for i in link :
    try:
        # object creation using YouTube
        # which was imported in the beginning 
        yt = YouTube(i)
        #downloading the video
        stream = yt.streams.first()
        stream.download(SAVE_PATH) 
    except:
        #to handle exception 
        print("Connection Error")

print("Task Completed")





