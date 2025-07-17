from TTS.api import TTS
import torch
import os
import torch.serialization

# ✅ Trusting custom classes for PyTorch 2.6+
from TTS.tts.models.xtts import Xtts, XttsAudioConfig, XttsArgs
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.config.shared_configs import BaseDatasetConfig

# 🛡️ Allow XTTS classes for safe loading
torch.serialization.add_safe_globals([
    XttsConfig, Xtts, BaseDatasetConfig, XttsAudioConfig, XttsArgs
])

print("🔄 Loading XTTS v2 model...")
device = "cuda" if torch.cuda.is_available() else "cpu"

# ✅ Load XTTS v2 ONLY
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2").to(device)
print("✅ XTTS v2 model loaded.")

# ✅ Expose supported languages only
available_languages = tts.languages

# Mapping of language codes to sample WAV paths
sample_wavs = {
    "en": "XTTS-v2/samples/en_sample.wav",
    "hi": "XTTS-v2/samples/hi_sample.wav",
    "de": "XTTS-v2/samples/de_sample.wav",
    "es": "XTTS-v2/samples/es_sample.wav",
    "fr": "XTTS-v2/samples/fr_sample.wav",
    "ja": "XTTS-v2/samples/ja-sample.wav",
    "pt": "XTTS-v2/samples/pt_sample.wav",
    "tr": "XTTS-v2/samples/tr_sample.wav",
    "zh-cn": "XTTS-v2/samples/zh-cn-sample.wav"
}

def synthesize_audio(text, language="en", output_path="output/output.wav"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Pick the reference WAV or default to English
    speaker_wav = sample_wavs.get(language, "XTTS-v2/samples/en_sample.wav")

    print("DEBUG: Synthesizing with language:", language)
    print("DEBUG: Using speaker wav:", speaker_wav)

    tts.tts_to_file(
        text=text,
        file_path=output_path,
        language=language,   # ✅ Important: use 'language'
        speaker_wav=speaker_wav
    )
    return output_path