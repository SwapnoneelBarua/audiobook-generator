import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
from text_extractor import extract_text
from tts_engine import synthesize_audio, sample_wavs
import os
import pygame
import uuid

# Map language code to readable name
LANGUAGE_MAP = {
    "en": "English", "hi": "Hindi", "de": "German", "es": "Spanish",
    "fr": "French", "ja": "Japanese", "pt": "Portuguese", "tr": "Turkish", "zh-cn": "Chinese"
}

# Reverse map for dropdown
LANGUAGE_CODES = {v: k for k, v in LANGUAGE_MAP.items()}


class AudiobookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audiobook Generator")
        self.root.geometry("900x700")
        self.root.configure(bg="#f0f2f5")
        self.current_output_path = None

        # Initialize pygame for audio playback
        pygame.mixer.init()

        title_label = tk.Label(root, text="🎧 Audiobook Generator", font=("Helvetica", 18, "bold"), bg="#f0f2f5")
        title_label.pack(pady=15)

        # Language dropdown
        self.language_code = tk.StringVar()
        lang_frame = tk.Frame(root, bg="#f0f2f5")
        lang_frame.pack(pady=10)

        tk.Label(lang_frame, text="🌐 Select Language:", font=("Helvetica", 12, "bold"), bg="#f0f2f5").pack(side=tk.LEFT)
        self.lang_dropdown = ttk.Combobox(
            lang_frame,
            values=list(LANGUAGE_MAP.values()),
            textvariable=self.language_code,
            state="readonly",
            width=20
        )
        self.lang_dropdown.set("English")  # Default
        self.lang_dropdown.pack(side=tk.LEFT, padx=10)

        open_btn = tk.Button(root, text="📘 Open PDF / TXT", command=self.load_file,
                             bg="#007bff", fg="white", font=("Helvetica", 12, "bold"), padx=12, pady=6)
        open_btn.pack(pady=5)

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier New", 11),
                                                   bg="white", fg="black", height=20)
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        self.progress = ttk.Progressbar(root, mode='indeterminate')
        self.progress.pack(pady=(0, 10), padx=20, fill=tk.X)
        self.progress.stop()

        action_frame = tk.Frame(root, bg="#f0f2f5")
        action_frame.pack(pady=5)

        tk.Button(action_frame, text="🔊 Generate Audio", command=self.synthesize,
                  bg="#28a745", fg="white", font=("Helvetica", 12, "bold"), padx=20).pack(side=tk.LEFT, padx=10)

        tk.Button(action_frame, text="▶️ Listen", command=self.play_audio,
                  bg="#6c757d", fg="white", font=("Helvetica", 12, "bold"), padx=15).pack(side=tk.LEFT, padx=10)

        self.status_label = tk.Label(root, text="", font=("Helvetica", 10), bg="#f0f2f5", fg="#555")
        self.status_label.pack(pady=(0, 10))

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF & Text Files", "*.pdf *.txt")])
        if file_path:
            text = extract_text(file_path)
            if text:
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, text)
                self.status_label.config(text=f"Loaded: {os.path.basename(file_path)}")
            else:
                messagebox.showerror("Error", "Could not extract text from the file.")

    def synthesize(self):
        text = self.text_area.get("1.0", tk.END).strip()
        if not text:
            messagebox.showerror("Error", "No text to synthesize.")
            return

        lang_name = self.language_code.get().strip()
        lang_code = LANGUAGE_CODES.get(lang_name)

        if not lang_code or lang_code not in sample_wavs:
            messagebox.showerror("Error", "Invalid or unsupported language selected.")
            return

        self.status_label.config(text="Synthesizing audio...")
        self.progress.start()

        try:
            if pygame.mixer.get_busy():
                pygame.mixer.music.stop()

            # Unique file to avoid permission error
            filename = f"output/output_{uuid.uuid4().hex[:8]}.wav"
            self.current_output_path = synthesize_audio(text, language=lang_code, output_path=filename)

            self.status_label.config(text=f"✅ Audio ready: {self.current_output_path}")
        except Exception as e:
            messagebox.showerror("TTS Error", str(e))
            self.status_label.config(text="❌ Error occurred.")
        finally:
            self.progress.stop()

    def play_audio(self):
        if not self.current_output_path or not os.path.exists(self.current_output_path):
            messagebox.showerror("Error", "No audio file to play.")
            return

        try:
            pygame.mixer.music.load(self.current_output_path)
            pygame.mixer.music.play()
            self.status_label.config(text="🎵 Playing audio...")
        except Exception as e:
            messagebox.showerror("Playback Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = AudiobookApp(root)
    root.mainloop()
