# import soundfile as sf
# from pysndfx import AudioEffectsChain
import os



ORIGINAL_PATH = os.getcwd() + "/wav_directory/original"


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
    print(findWavOriginal(ORIGINAL_PATH))
