import os
import librosa
import soundfile as sf
from pydub import AudioSegment

def loadAudio(inputPath, outputPath):
    frameRate = 44100
    extension = os.path.splitext(inputPath)[1].lower()

    possibleExtensions = [".mp3", ".flac", ".ogg", ".m4a"]

    if extension in possibleExtensions:
        audio = AudioSegment.from_file(inputPath)
        audio = audio.set_frame_rate(frameRate).set_channels(1)
        audio.export(outputPath, format = "wav")

    elif extension == ".wav":
        audio, sr = librosa.load(inputPath, sr= frameRate, mono=True)
        sf.write(outputPath, audio, sr, subtype='PCM_16')

    return outputPath

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the user-uploaded audio file")
    parser.add_argument("--output", required=True, help="Path to save the processed WAV file")
    args = parser.parse_args()

    base_name = os.path.splitext(os.path.basename(args.input))[0]
    output_file_path = os.path.join(args.output, base_name + ".wav")

    loadAudio(args.input, output_file_path)
