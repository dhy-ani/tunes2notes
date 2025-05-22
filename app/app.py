import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.preprocessing.audioLoader import loadAudio
from src.preprocessing.isolatePiano import isolate_piano
from src.preprocessing.wavToMidi import wav_to_midi
from src.preprocessing.midiToPDF import midi_to_pdf

TEMP_DIR = "temp"
MIDI_DIR = "midi_output"
PDF_DIR = "sheet_output"
os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(MIDI_DIR, exist_ok=True)
os.makedirs(PDF_DIR, exist_ok=True)

st.title("Welcome to Tunes2Notes...Convert Songs to Music Sheets")

uploaded_file = st.file_uploader("Uploaded an audio file", type=["mp3", "wav", "flac", "m4a"])


if uploaded_file:
    st.info("Processing...")
    filename = os.path.splittext(uploaded_file.name)[0]
    input_path = os.path.join(TEMP_DIR, uploaded_file.name)
    
    print("Saving file")
    
    with open(input_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        
    wav_path = os.path.join(TEMP_DIR , f"{filename}.wav")
    
    loadAudio(input_path, TEMP_DIR) #temp is output
    
    #isolate piano
                        #output of audioloader, name of file
    piano_wav = os.path.join(TEMP_DIR, "piano.wav")
    isolate_piano(wav_path, TEMP_DIR)
    
    
    #WAV TO MIDI
    midi_path = os.path.join(MIDI_DIR, F"{filename}.mid")
    wav_to_midi(piano_wav, midi_path)
    
    pdf_path = midi_to_pdf(midi_path, PDF_DIR)
    
    with open(pdf_path, "rb") as f:
        st.download_button("Your Sheet PDF is ready", f, file_name=f"{filename}.pdf")