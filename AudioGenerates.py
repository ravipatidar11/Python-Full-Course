from gtts import gTTS

text="Hi Ravi Welcome To Python Programming Language"

tts=gTTS(text=text,lang="en")

tts.save("voice.mp3")

print("Audio Saved Successfully")