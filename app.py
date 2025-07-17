import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
from text_extractor import extract_text
from tts_engine import synthesize_audio, available_languages
import os

class AudiobookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audiobook Generator")
        self.root.geometry("900x700")
        self.root.configure(bg="#f0f2f5")

        # App title
        title_label = tk.Label(
            self.root,
            text="🎧 Audiobook Generator",
            font=("Helvetica", 18, "bold"),
            bg="#f0f2f5",
            fg="#333"
        )
        title_label.pack(pady=15)

        # Language selector
        self.language_code = tk.StringVar()
        lang_frame = tk.Frame(self.root, bg="#f0f2f5")
        lang_frame.pack(pady=(5, 10))

        lang_label = tk.Label(
            lang_frame,
            text="🌐 Select Language:",
            font=("Helvetica", 12, "bold"),
            bg="#f0f2f5"
        )
        lang_label.pack(side=tk.LEFT, padx=(0, 10))

        self.lang_dropdown = ttk.Combobox(
            lang_frame,
            textvariable=self.language_code,
            values=sorted(available_languages),
            state="readonly",
            width=20
        )
        self.lang_dropdown.pack(side=tk.LEFT)
        self.lang_dropdown.current(0)

        # Open file button
        open_btn = tk.Button(
            self.root,
            text="📘 Open PDF / TXT",
            command=self.load_file,
            bg="#007bff",
            fg="white",
            font=("Helvetica", 12, "bold"),
            padx=12,
            pady=6
        )
        open_btn.pack(pady=5)

        # Text display
        self.text_area = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            font=("Courier New", 11),
            bg="white",
            fg="black",
            height=20
        )
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        # Generate audio button
        synth_btn = tk.Button(
            self.root,
            text="🔊 Generate Audio",
            command=self.synthesize,
            bg="#28a745",
            fg="white",
            font=("Helvetica", 13, "bold"),
            padx=20,
            pady=10
        )
        synth_btn.pack(pady=15)

        # Status label
        self.status_label = tk.Label(
            self.root,
            text="",
            font=("Helvetica", 10),
            bg="#f0f2f5",
            fg="#555"
        )
        self.status_label.pack(pady=(0, 10))

    def load_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("PDF & Text Files", "*.pdf *.txt")]
        )
        if file_path:
            text = extract_text(file_path)
            if text:
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, text)
                self.status_label.config(text=f"Loaded: {os.path.basename(file_path)}")
            else:
                messagebox.showerror("Error", "Could not extract text from the file.")
                self.status_label.config(text="")

    def synthesize(self):
        text = self.text_area.get("1.0", tk.END).strip()
        if not text:
            messagebox.showerror("Error", "No text to synthesize.")
            return

        lang_code = self.language_code.get().strip()
        if not lang_code:
            messagebox.showerror("Error", "Please select a language.")
            return

        self.status_label.config(text="Synthesizing audio... Please wait.")

        try:
            output_file = synthesize_audio(
                text,
                language=lang_code,
                output_path="output/output.wav"
            )
            messagebox.showinfo("Success", f"Audio generated:\n{output_file}")
            self.status_label.config(text=f"Audio generated: {output_file}")
            os.startfile(output_file)
        except Exception as e:
            messagebox.showerror("TTS Error", str(e))
            self.status_label.config(text="Error occurred during synthesis.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AudiobookApp(root)
    root.mainloop()
