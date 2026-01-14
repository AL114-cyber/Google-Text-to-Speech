# Google-Text-to-Speech
gTTS generates an audio file from text, which we can then play. Let's install it and IPython.display to play the audio.

Let's review the final version of the RoboSpeaker code that successfully works in Google Colab.

1. Import necessary libraries:
gTTS: This is the Google Text-to-Speech library, which converts text into speech and saves it as an audio file.
IPython.display: This module is used to play audio files directly within the Colab notebook.
os: This module provides a way to interact with the operating system, for example, to remove files.

2. Main execution block (if __name__ == '__main__':):
This ensures the code inside only runs when the script is executed directly (not when imported as a module). It prints a welcome message and then enters an infinite loop (while True) to continuously take user input.

3. Exit condition:
The loop checks if the user types "quit" (case-insensitive) to gracefully shut down the RoboSpeaker.

4. Text-to-Speech conversion and playback (inside a try-except block):
This is the core functionality. It's wrapped in a try-except block to handle potential errors gracefully.

tts = gTTS(text=x, lang='en', slow=False): Creates a gTTS object. text is your input, lang='en' sets the language to English, and slow=False makes the speech normal speed.
audio_file = 'temp_speech.mp3': Defines a temporary filename for the audio.
tts.save(audio_file): Saves the generated speech into the temp_speech.mp3 file.
display(Audio(audio_file, autoplay=True)): This is the crucial part for Colab. It takes the saved audio file and plays it automatically in the notebook output.
os.remove(audio_file): (Commented out) This line would delete the temporary audio file after playback. It's often good practice to clean up temporary files, but it's commented out here so you can inspect the file if needed. If uncommented, it ensures your Colab environment doesn't get cluttered.
except Exception as e: If any error occurs during this process, it catches the exception and prints an error message.

This structured approach makes the RoboSpeaker robust and ensures it functions correctly within the Google Colab environment.

To make the RoboSpeaker work on Windows 11, we can use the pyttsx3 library. This library provides a cross-platform interface to text-to-speech engines. Let's install it first.
