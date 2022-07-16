from moviepy.editor import *
import sys, os
from pydub import AudioSegment

FILLER = AudioSegment.from_file("/home/schimi/Documents/GitHub/python_video_maker/folder/nothing.mp3",format = "mp3")

def create_vid():
    i = 0
    audioclip = FILLER
    print(os.listdir(os.path.join("folder")))
    for file in os.listdir(os.path.join("folder")):
        if os.path.isfile(os.path.join("folder",file)) and file.startswith("joke"):
            print(file)
            audioclip += AudioSegment.from_mp3(f"/home/schimi/Documents/GitHub/python_video_maker/folder/joke{i}.mp3") + FILLER 
            i += 1
    audioclip.export("/home/schimi/Documents/GitHub/python_video_maker/folder/finalaudio.mp3")
    audioclip_final = AudioFileClip(os.path.join("folder", "finalaudio.mp3"))
    vidclip = VideoFileClip(os.path.join("folder", "Minecraft.mp4"))
    finalclip = vidclip.set_audio(audioclip_final)
    finalclip.write_videofile(os.path.join("folder", "finalvid.mp4"), fps = 30)

create_vid()
