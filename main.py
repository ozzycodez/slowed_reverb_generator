import soundfile as sf
from pysndfx import AudioEffectsChain
import os



ORIGINAL_PATH = os.getcwd() + "/wav_directory/original"
SLOWED_REVERB_PATH = os.getcwd() + "/wav_directory/slowed_reverb"
SONG_NAME = ""



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
            size = len(name)
            global SONG_NAME
            SONG_NAME = name[:size- 4]
            wav_orignal_path = os.path.join(dir, name)
            return wav_orignal_path 



if __name__ == "__main__":
    ORIGINAL_WAV_FILE = findWavOriginal(ORIGINAL_PATH)

    s, rate = sf.read(ORIGINAL_WAV_FILE)
    fx = (
        AudioEffectsChain()
        .speed(0.8)
    )
    s = fx(s, sample_in=rate)


    NEW_WAV_FILE = SONG_NAME + "_slowed_reverb.wav"
    SLOWED_REVERB_PATH_SAVE = os.path.join(SLOWED_REVERB_PATH,NEW_WAV_FILE)
    sf.write(SLOWED_REVERB_PATH_SAVE,s,rate, 'PCM_16')


