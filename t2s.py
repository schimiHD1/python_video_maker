import gtts
import os


def create_voice(text,number):
    tts = gtts.gTTS(f"{text[0]}{text[-1]}","com","en",True)
    name = f"joke{number}.mp3"
    tts.save(name)
    os.replace(f"/home/schimi/Documents/GitHub/python_video_maker/{name}",f"/home/schimi/Documents/GitHub/python_video_maker/folder/{name}" )

if __name__ =="__main__":
    create_voice(["Hello Mrs","I will surely die now"], 2)