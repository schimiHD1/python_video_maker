from moviepy.editor import *
import sys,os
os.path.join("/home/schimi/Documents/GitHub/python_video_maker/folder/")
FILLER = AudioFileClip("nothing.mp3")
def create_vid():
    for i in range(len(os.listdir("/home/schimi/Documents/GitHub/python_video_maker/folder/"))):
        audioclip = FILLER + AudioFileClip(f"joke{i}.mp3")
    vidclip = VideoFileClip("Minecraft.mp4")
    finalclip = vidclip.set_audio(audioclip)
    finalclip.write_videofile("finalvid.mp4",fps = 30)
create_vid()