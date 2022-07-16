from moviepy.editor import *
import sys, os

FILLER = AudioFileClip(os.path.join("folder", "nothing.mp3"))

def create_vid():
    i = 0
    for file in os.listdir(os.path.join("folder"):
        if os.path.isfile(file):
            audioclip = FILLER + AudioFileClip(os.path.join("folder", f"joke{i}.mp3"))
            i += 1
    
    vidclip = VideoFileClip(os.path.join("folder", "Minecraft.mp4"))
    finalclip = vidclip.set_audio(audioclip)
    finalclip.write_videofile(os.path.join("folder", "finalvid.mp4"), fps = 30)

create_vid()
