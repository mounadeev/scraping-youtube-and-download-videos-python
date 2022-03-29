# Downloading a single video

# importing the module 
from pytube import YouTube

# where to save 
SAVE_PATH = " " #to_do 

# link of the video to be downloaded 
link = " "

try:
    # object creation using YouTube
    # which was imported in the beginning
    yt = YouTube(link)
except:
    print("connection Error")

# To print title
print("Title:", yt.title)

# To get number of views
print("Views:", yt.views)

# To get the length of video
print("Duration: ", yt.length)

# To get description
print("Desciption: ", yt.description)

# To get ratings
print("Rationg:", yt.rating)


try:
    #downloading the video
    stream = yt.streams.first()
    stream.download(SAVE_PATH)       
except:
    print("some error")

print("Task Completed")

