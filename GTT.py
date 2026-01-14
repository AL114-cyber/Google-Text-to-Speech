from gtts import gTTS
from IPython.display import Audio, display
import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 2.0. Created by Harry (now Colab compatible with gTTS!)")
    while True:
        x = input("Enter what you want me to speak: ")
        if x.lower() == "quit":
            print("RoboSpeaker shut down.")
            break
        try:
            tts = gTTS(text=x, lang='en', slow=False)
            # Save the audio to a temporary file
            audio_file = 'temp_speech.mp3'
            tts.save(audio_file)
            
            # Play the audio file
            display(Audio(audio_file, autoplay=True))
            
            # Clean up the temporary file
            # os.remove(audio_file) # Uncomment this if you want to delete the file immediately
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")
