from moviepy.editor import VideoFileClip
import whisper

# Function to extract audio from video
def extract_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)

# Function to transcribe audio to text
def transcribe_audio(file_path):
    # Load the Whisper model
    print("Beginning transcription")
    try:
        model = whisper.load_model("base")
        print("Model Loaded, transcription beginning")
        # Transcribe the audio
        result = model.transcribe(file_path)

        # Return the transcription
        return result["text"]
    except:
        print("error Processing results")

# Main process
video_path = 'pathtovideo.'
audio_path = 'extracted_audio.wav'
audio_file_path = audio_path  # Use the extracted audio file path

# Extract audio from video
extract_audio(video_path, audio_path)

# Transcribe audio
transcription = transcribe_audio(audio_file_path)

# Save the transcription to a text file
with open('transcribe.txt', 'w') as file:
    file.write(transcription)

print("Transcription saved to 'transcribe.txt'")
