# 🗣️ Audiobook Generator with XTTS v2

A fully offline/online AI-based audiobook generator built using 🐸TTS XTTS v2 and Python. Supports multilingual synthesis, voice cloning, and a GUI interface via Tkinter or Streamlit.

---

## 🔧 Features

- 🎙️ Multilingual text-to-speech using XTTS v2
- 🧠 Speaker cloning via sample WAVs
- 💻 GUI-based control via Tkinter / Streamlit
- 📦 Offline support with local models
- 📁 Build to `.exe` for easy deployment (PyInstaller)

---

## 📂 Folder Structure
audiobook-generator/
├── app.py                         # Main Streamlit/Tkinter app
├── tts_engine.py                 # XTTS v2-based TTS synthesis logic
├── audiobook_app_ui.spec        # PyInstaller build file
├── requirements.txt             # All pip requirements
├── environment.yml              # Conda environment file
├── README.md                    # Detailed project overview
├── LICENSE                      # (e.g., MIT)
├── .gitignore                   # Ignore compiled files and virtualenv
├── XTTS-v2/
│   ├── config.json
│   ├── model.pth
│   ├── vocoder.pth
│   └── samples/
│       ├── en_sample.wav
│       ├── hi_sample.wav
│       └── fr_sample.wav


🛠️ Build EXE (Optional)
pyinstaller audiobook_app_ui.spec

📦 Requirements
Install dependencies:
pip install -r requirements.txt

Or use Conda:
conda env create -f environment.yml
conda activate audiobook-generator

