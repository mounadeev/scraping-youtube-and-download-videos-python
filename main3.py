# Download multiple videos using File Handling

from pytube import YouTube 

# where to save 
SAVE_PATH = "E:/" #to_do 
  
# link of the video to be downloaded 
# opening the file 
link=open('links_file.txt','r') 

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
