"""/
    author      :: shemiradiance@gmail.com
    title       :: Pdf -> Audio
    description :: reading pdf as audio
    date        :: 11/01/2023
/"""

import sys
import pyttsx3
from pypdf import PdfReader

# <Read PDF content>
def read_pdf(pdfFile: str):
    reader = PdfReader(pdfFile)
    page = reader.pages[0]
    print(page.extract_text())


# <Say PDF content>
def say(text: str, rate: int = 125, volume: float = 1.0, voice: int = 0):
    """
    text   :: the string to say
    rate   :: Speed at which it speaks
    volume :: How loud the audio is, from 0 - 1.0
    voice  :: 0 -> male, 1 -> female
    """
    engine = pyttsx3.init()
    
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

