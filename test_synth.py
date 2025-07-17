from TTS.api import TTS
import torch
import os

# Trusting custom classes for PyTorch 2.6+
from TTS.tts.models.xtts import Xtts, XttsAudioConfig, XttsArgs
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.config.shared_configs import BaseDatasetConfig

torch.serialization.add_safe_globals([
    XttsConfig, Xtts, BaseDatasetConfig, XttsAudioConfig, XttsArgs
])

# Load XTTS v2
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")

# Make sure the speaker wav exists
speaker_wav = "XTTS-v2/samples/hi_sample.wav"

if not os.path.exists(speaker_wav):
    print("ERROR: Sample wav not found!")
    exit(1)

# Synthesize
print("Synthesizing...")
tts.tts_to_file(
    text="This is a test of English synthesis.",
    file_path="output/test_output.wav",
    speaker_wav=speaker_wav,
    language="en"  # <-- IMPORTANT: use 'language' not 'lang'
)
print("Done.")
