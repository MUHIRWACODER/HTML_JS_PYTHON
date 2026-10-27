import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Music Player")
        self.root.geometry("400x200")

        # Initialize Pygame Mixer
        pygame.mixer.init()

        # UI Title Label
        self.label = tk.Label(root, text="Music Player", font=("Arial", 16, "bold"))
        self.label.pack(pady=10)

        # Track name label
        self.track_label = tk.Label(root, text="No track selected", font=("Arial", 10), fg="gray")
        self.track_label.pack(pady=5)

        # Buttons
        self.load_btn = tk.Button(root, text="Select Music File", width=20, command=self.load_music)
        self.load_btn.pack(pady=5)

        self.play_btn = tk.Button(root, text="Play", width=20, bg="lightgreen", command=self.play_music)
        self.play_btn.pack(pady=5)

        self.pause_btn = tk.Button(root, text="Pause / Unpause", width=20, bg="lightyellow", command=self.pause_music)
        self.pause_btn.pack(pady=5)

        self.stop_btn = tk.Button(root, text="Stop", width=20, bg="lightcoral", command=self.stop_music)
        self.stop_btn.pack(pady=5)

        self.current_file = ""
        self.is_paused = False

    def load_music(self):
        # Open file dialog to choose an MP3 or WAV file
        self.current_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if self.current_file:
            filename = os.path.basename(self.current_file)
            self.track_label.config(text=f"Loaded: {filename}", fg="black")

    def play_music(self):
        if self.current_file:
            pygame.mixer.music.load(self.current_file)
            pygame.mixer.music.play()
            self.is_paused = False
        else:
            self.track_label.config(text="Please select a file first!", fg="red")

    def pause_music(self):
        if not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True
        else:
            pygame.mixer.music.unpause()
            self.is_paused = False

    def stop_music(self):
        pygame.mixer.music.stop()
        self.is_paused = False

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()