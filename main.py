import tkinter as tk
from tkinter import filedialog
from gtts import gTTS
import pygame
import PyPDF2
import os
import threading

pygame.mixer.init()

audio_file = "C:/text_to_audio/audio.mp3"
is_playing = False
is_paused = False
pages = []

def load_pdf(file):
    global pages
    pdf_reader = PyPDF2.PdfReader(file)
    pages = [page.extract_text().replace("\n", " ") for page in pdf_reader.pages if page.extract_text()]
    print(f"Loaded {len(pages)} pages from the PDF.")

def generate_audio():
    global audio_file
    text = " ".join(pages)
    tts = gTTS(text, lang='en')

    # saved audio in separate thread to avoid blocking the GUI
    def save_audio():
        if os.path.exists(audio_file):
            os.remove(audio_file)
        tts.save(audio_file)
        print(f"Audio file saved: {audio_file}")
        update_play_button()

    audio_thread = threading.Thread(target=save_audio, daemon=True)
    audio_thread.start()

def update_play_button():
    btn_play.config(state=tk.NORMAL, text="Play") 

def play_audio():
    global is_playing, is_paused
    if not is_playing:
        if not os.path.exists(audio_file):
            print("No audio file found")
            generate_audio()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        is_playing = True
        print("Playing audio")
    elif is_paused:
        pygame.mixer.music.unpause()
        is_paused = False
        print("Resume audio")

def pause_audio():
    global is_paused
    if is_playing and not is_paused:
        pygame.mixer.music.pause()
        is_paused = True
        print("Audio paused")

def stop_audio():
    global is_playing, is_paused
    pygame.mixer.music.stop()
    is_playing = False
    is_paused = False
    print("Audio stopped")

def open_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        print(f"Selected file: {file_path}")
        load_pdf(file_path)
        generate_audio()

root = tk.Tk()
root.title("PDF to Audio Reader")

btn_open = tk.Button(root, text="Open PDF", command=open_pdf)
btn_play = tk.Button(root, text="Play", command=play_audio)
btn_pause = tk.Button(root, text="Pause", command=pause_audio)
btn_stop = tk.Button(root, text="Stop", command=stop_audio)

btn_open.pack(pady=5)
btn_play.pack(pady=5)
btn_pause.pack(pady=5)
btn_stop.pack(pady=5)

root.mainloop()
