# PDF to Audio Reader
This project converts a PDF file into an audio format using text-to-speech technology. 
The program allows users to select a PDF file, convert its text into speech, and control the audio playback (play, pause, stop) through a simple graphical user interface (GUI).

## Features
**Load PDF** : Allows the user to select a PDF file for conversion.

**Text-to-Speech**: Converts the content of the PDF into an audio file using Google Text-to-Speech (gTTS).

**Audio Control**: Includes play, pause, and stop functionality for controlling the audio playback.

**Easy-to-Use GUI**: Built with Tkinter to provide an intuitive and user-friendly interface.

## Requirements
- Python 3.x

- Libraries:
*tkinter* (for GUI),
*gTTS* (for text-to-speech conversion),
*pygame* (for audio playback),
*PyPDF2* (for extracting text from PDF files)

To install the required libraries, you can run:

    pip install gTTS pygame PyPDF2

## How to use:
- Open the Program: Run the Python script main.py.
- Select a PDF: Click on the "Open PDF" button to open a file dialog. Choose the PDF file you want to convert.
- Run again the script main.py and click the "Play" button to start playing the audio.
