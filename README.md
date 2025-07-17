# 📚 Audiobook Generator using XTTS v2

A high-quality offline and online **audiobook generation tool** built with 🐍 Python, 🐸 TTS (XTTS v2), and 🎧 voice cloning. Converts long-form text into human-like speech using multilingual synthesis.

## 🚀 Features

- ✅ **Multilingual Voice Synthesis** using [XTTS v2](https://huggingface.co/coqui/XTTS-v2)
- 🗣️ **Voice Cloning Support** via speaker reference `.wav` files
- 🎛️ Tkinter-based Graphical User Interface (GUI)
- 🌐 Supports both **online and offline** generation modes
- 📁 Manual control of output language, chunking, and saving
- 🎧 Integrated audio playback and download options

---

## 📦 Installation & Setup

### 1️⃣ Clone This Repository

```bash
git clone https://github.com/SwapnoneelBarua/audiobook-generator
cd audiobook-generator
```
### 2️⃣ Clone XTTS v2 Model Files (Required)
Due to GitHub size limits, XTTS v2 model files are not included in this repo.

Please clone them from Hugging Face:
```bash
git lfs install
git clone https://huggingface.co/coqui/XTTS-v2

```
Place the downloaded contents in:
```bash
D:\AI projects\audiobook_generator\XTTS-v2\
```
Or wherever your local path is — just update xtts_path in your code accordingly if changed.

### 3️⃣ Setup Conda Environment (Recommended)
Using environment.yml:
```bash
conda env create -f environment.yml
conda activate audiobookenv
```
If environment.yml not available, create manually:

```bash
conda create -n audiobookenv python=3.10
conda activate audiobookenv
pip install -r requirements.txt
```
### 🔧 Manual Requirements (if needed)

Make sure the following packages are installed:
```bash
pip install torch==2.1.2 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install TTS==0.22.0
pip install streamlit
pip install pydub numpy soundfile scipy
```
Also ensure ffmpeg is installed and added to your system PATH.

### ▶️ Run the Application
Run the main app from the terminal:
```bash
python audiobook_app_ui.py
```
The Tkinter GUI will open.

### 🎛️ How to Use
1.📝 Paste or Load any long text (story, chapter, content).

2.🌍 Select a Language from the dropdown.

3.🎙️ Choose a Speaker Sample (e.g., en_sample.wav) — stored under:
```bash
XTTS-v2/samples/
```
4.🧠 Click Generate Audio.

5.🎧 You can listen, pause/resume, or save the generated audio.
### 📁 Sample Path and Files
Make sure your speaker samples are placed at:
```bash
XTTS-v2/samples/en_sample.wav
XTTS-v2/samples/hi_sample.wav
```
You can add more voices and samples as required.

### ⚙️ Notes
XTTS v2 supports speaker cloning with multilingual output.

The app automatically splits long input texts into smaller chunks for smoother synthesis.

GPU is recommended for faster generation.

Ensure PyTorch and 🐸TTS are correctly installed with torch.serialization.add_safe_globals() applied (handled in code).

Internet is only required during first-time Hugging Face model download.

🤝 Contribution
Pull requests are welcome! Fork the repo, create a feature branch, and submit your improvements.

📜 License
This project is licensed under the MIT License.

👤 Developed By
Swapnoneel Barua

🔗 GitHub

🔗 LinkedIn
