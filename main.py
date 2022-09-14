from curses.ascii import SO
import soundfile as sf
from pysndfx import AudioEffectsChain
import os
from pydub import AudioSegment



ORIGINAL_PATH = os.getcwd() + "/wav_directory/original"
SLOWED_REVERB_PATH = os.getcwd() + "/wav_directory/slowed_reverb"
SONG_NAME = ""




#if MP3 input in 'original' directory, will convert to WAV format, so soundfile and pysndfx can work
def convertMp3ToWav(dir):
    TEMP_PATH = ORIGINAL_PATH + "/" + SONG_NAME + ".wav"
    sound = AudioSegment.from_mp3(dir)
    sound.export(TEMP_PATH, format="wav")




#converts WAV to MP3 (To have playable end product)
def convertWavToMp3(dir):
    TEMP_PATH = SLOWED_REVERB_PATH + SONG_NAME
    sound = AudioSegment.from_wav(dir)
    sound.export(TEMP_PATH, format="mp3")




#will find name of audio file, stored in the "original" directory
def findName(dir):
    fileNames = os.listdir(dir)
    count = 0

    for files in fileNames:
        count += 1
    
    if count != 1:
        return "ERROR, make sure there is only 1 file in '/wav_directory/original"
    else:
        for name in fileNames:
            size = len(name)
            global SONG_NAME
            SONG_NAME = name[:size- 4]




# function will check "/wav_directory/original" and check if there is only 1 .wav file in there
def findWavOriginal(dir):
    fileNames = os.listdir(dir)
    count = 0

    for files in fileNames:
        count += 1
    
    if count != 1:
        return "ERROR, make sure there is only 1 file in '/wav_directory/original"
    else:
        for name in fileNames:
            wav_orignal_path = os.path.join(dir, name)
            return wav_orignal_path 



if __name__ == "__main__":
    findName(ORIGINAL_PATH)
    convertMp3ToWav(ORIGINAL_PATH + "/" + SONG_NAME + ".mp3")
