import argparse
import os
from music21 import converter, environment

def midi_to_pdf(midi_path, output_dir="Sheets"):
    us = environment.UserSettings()
    us['lilypondPath'] = 'C:\\lilypond\\bin\\lilypond.exe'
    
    score = converter.parse(midi_path)
    os.makedirs(output_dir, exist_ok=True)
    
    pdf_path = os.path.join(output_dir, os.path.splittext(os.path.basename(midi_path))[0]+".pdf")
    score.write('lily.pdf', fp = pdf_path)
    
    print(f"PDF GENERATED ! Find at {pdf_path}")
    
    return pdf_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to MIDI file")
    parser.add_argument("--outdir", default="sheet_output", help="Output folder for PDF")
    args = parser.parse_args()

    midi_to_pdf(args.input, args.outdir)