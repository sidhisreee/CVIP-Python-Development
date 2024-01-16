import sounddevice  # For recording audio
from scipy.io.wavfile import write  # For saving audio as a .wav file

# Sample rate (44.1 kHz is a common sample rate for audio)
fs = 44100

# Prompt user for recording duration in seconds
second = int(input("Enter the time duration in seconds: "))

print("Recording...\n")

# Start recording using the given sample rate, duration, and channel configuration
record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)

# Wait for the recording to finish
sounddevice.wait()

# Save the recorded audio as a .wav file
write("out.wav", fs, record_voice)

print("Successfully recorderd...\n Recording saved...")