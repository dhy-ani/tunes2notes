import argparse
import note_seq

import os
from magenta.models.onsets_frames_transcription import infer_util
from magenta.models.onsets_frames_transcription import audio_processor

def wav_to_midi(
    wav_path,
    output_path,
    onset_threshold: float=0.5,
    frame_threshold:float = 0.5,
    ):

    print("Loading audio for transcription!")
    audio, sampleRate = audio_processor.load_audio(wav_path, 16000)
    
    print("converting WAV to MIDI...")
    sequence = infer_util.transcribe_overlapping_sections(
        audio,
        sample_rate=sampleRate,
        model_bundle=note_seq.sequence_proto_to_midi_file, #default checkpoint
        onset_threshold=onset_threshold,
        frame_threshold=frame_threshold
    )
    
    note_seq.sequence_proto_to_midi(sequence, output_path)
    print(f"MIDI saved to {output_path}")
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the piano WAV file")
    parser.add_argument("--output", required=True, help="Path to save the output MIDI")
    parser.add_argument("--onset", type=float, default=0.5, help="Onset threshold")
    parser.add_argument("--frame", type=float, default=0.5, help="Frame threshold")
    args = parser.parse_args()

    wav_to_midi(args.input, args.output, args.onset, args.frame)