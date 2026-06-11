#Step1 a: Setup text to speech-TTS-model (gTTS)
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    langauge="en"

    audioobj = gTTS(
        text = input_text,
        lang = langauge,
        slow = False,
    )
    audioobj.save(output_filepath)

input_text = "Hi, This is AI with DS!"
#text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

#Step1 b: Setup text to speech-TTS-model (ElevenLabs)
from dotenv import load_dotenv
load_dotenv()
import os
import elevenlabs
from elevenlabs.client import ElevenLabs


ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")
print(ELEVENLABS_API_KEY)

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice="ohvvU75FpBEB8fdaLOMh",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

#text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3")

#Step2 : Use model for text output to voice 
import subprocess
import platform

def text_to_speech_with_gtts(input_text, output_filepath, autoplay=False):
    langauge="en"

    audioobj = gTTS(
        text = input_text,
        lang = langauge,
        slow = False,
    )
    audioobj.save(output_filepath)
    if not autoplay:
        return output_filepath
    os_name = platform.system()
    try:
        if os_name == "Darwin": #macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows": #Windows
            os.startfile(output_filepath)
        elif os_name == "Linux":
            subprocess.run(['aplay', output_filepath])
        else:
            raise OSError("Unsuppported operating system")
    except Exception as e:
        print(f"An error occcured while trying to play the audio: {e}")

# input_text = "Hi, This is AI with DS, autoplay testing!"
# text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice="ohvvU75FpBEB8fdaLOMh",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin": #macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows": #Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer"{output_filepath}").PlaySync();'])
        elif os_name == "Linux":
            subprocess.run(['aplay', output_filepath])
        else:
            raise OSError("Unsuppported operating system")
    except Exception as e:
        print(f"An error occcured while trying to play thee audio: {e}")

# text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")