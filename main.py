import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from text_extractor import extract_text
from tts_engine import synthesize_audio  # ✅ updated import
import os

class AudiobookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audiobook Generator - YourTTS")
        self.root.geometry("800x600")

        # Text display area
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        # Menu bar for file loading
        menubar = tk.Menu(root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open PDF/TXT", command=self.load_file)
        menubar.add_cascade(label="File", menu=file_menu)
        root.config(menu=menubar)

        # Generate Audio Button
        synth_btn = tk.Button(
            self.root, 
            text="🔊 Generate Audio", 
            command=self.synthesize, 
            bg="#4CAF50", 
            fg="white", 
            font=("Arial", 12, "bold")
        )
        synth_btn.pack(pady=10)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF & Text Files", "*.pdf *.txt")])
        if file_path:
            text = extract_text(file_path)
            if text:
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, text)
            else:
                messagebox.showerror("Error", "Could not extract text.")

    def synthesize(self):
        text = self.text_area.get("1.0", tk.END).strip()
        if not text:
            messagebox.showerror("Error", "No text to synthesize!")
            return

        try:
            output_file = synthesize_audio(text)
            messagebox.showinfo("Success", f"Audio saved to:\n{output_file}")
            os.startfile(output_file)  # Auto-play output.wav (Windows only)
        except Exception as e:
            messagebox.showerror("TTS Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = AudiobookApp(root)
    root.mainloop()
