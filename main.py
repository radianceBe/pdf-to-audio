"""/
    author      :: shemiradiance@gmail.com
    title       :: Pdf -> Audio
    description :: reading pdf as audio
    date        :: 11/01/2023
/"""

import sys
import datetime

import pyttsx3

from pypdf import PdfReader
from datetime import datetime

reader = PdfReader(pdfFile)
engine = pyttsx3.init()

# <Read PDF content>
def read_pdf(pdfFile: str):
    page = reader.pages[0]
    print(page.extract_text())


# <Say PDF content>
def say(text: str, rate: int = 125, volume: float = 1.0, voice: int = 0, saveAudio: bool = false, filename: str = ""):
    """
    text   :: the string to say
    rate   :: Speed at which it speaks
    volume :: How loud the audio is, from 0 - 1.0
    voice  :: 0 -> male, 1 -> female
    """
    
    # - Get engine Properties
    # rate   = engine.getProperty("rate")
    # volume = engine.getProperty("volume")
    voices  = engine.getProperty("voice")

    # - Set engine Properties
    engine.setProperty("rate", rate)
    engine.setProperty("volume", volume)
    engine.setProperty("voice", voices[voice].id)
    
    engine.say(text)
    engine.runAndWait()

    # - Save audio as mp3
    if len(filename) == 0:
        # - Generate filename
        cnow = datetime.now()
        filename = f"PTA-Audio-{cnow}.mp3"
    elif not filename.endswith(".mp3"):
        filename = f"{filename}.mp3"

    if saveAudio:
        engine.save_to_file(text, filename)


# <Saving Audio as MP3>
# def save(text: str, filename: str):
#     engine

read_pdf("library\\EDU 215  - Copy.pdf")