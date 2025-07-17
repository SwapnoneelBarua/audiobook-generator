# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files
import os

# ✅ Collect required data files from TTS (e.g., VERSION)
tts_datas = collect_data_files("TTS")

# ✅ Add speaker WAV files from local samples folder
speaker_wavs = [
    ("XTTS-v2/samples/en_sample.wav", "XTTS-v2/samples"),
    ("XTTS-v2/samples/hi_sample.wav", "XTTS-v2/samples"),
    ("XTTS-v2/samples/fr_sample.wav", "XTTS-v2/samples"),  # Add more if needed
    ("XTTS-v2/samples/de_sample.wav", "XTTS-v2/samples"),
    ("XTTS-v2/samples/es_sample.wav", "XTTS-v2/samples"),
    ("XTTS-v2/samples/ja-sample.wav", "XTTS-v2/samples"),
    ("XTTS-v2/samples/pt_sample.wav", "XTTS-v2/samples"),
    ("XTTS-v2/samples/tr_sample.wav", "XTTS-v2/samples"),
    ("XTTS-v2/samples/zh-cn-sample.wav", "XTTS-v2/samples"),
]

# Combine both data sets
all_datas = tts_datas + speaker_wavs

a = Analysis(
    ['audiobook_app_ui.py'],
    pathex=[],
    binaries=[],
    datas=all_datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='audiobook_app_ui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='audiobook_app_ui',
)
