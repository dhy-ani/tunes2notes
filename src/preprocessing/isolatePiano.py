import os
import shutil
from spleeter.separator import Separator

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

def isolate_piano(inputPath, outputPath):
    inputAudio = os.path.join(BASE_DIR, inputPath)

    separator = Separator("spleeter:5stems")

    tempFolder = os.path.join(BASE_DIR, "spleeterOutput")
    os.makedirs(tempFolder, exist_ok=True)

    separator.separate_to_file(inputAudio, tempFolder)

    audioFile = os.path.splitext(os.path.basename(inputAudio))[0]
    pianoAudio = os.path.join(tempFolder, audioFile, "piano.wav")

    outputPath = os.path.join(outputPath, "piano.wav")

    shutil.copy(pianoAudio, outputPath)

    shutil.rmtree(tempFolder)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the user-uploaded audio file")
    parser.add_argument("--output", required=True, help="Path to save the processed WAV file")
    args = parser.parse_args()
    
    isolate_piano(args.input, args.output)
