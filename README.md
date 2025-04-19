# deduplication-helper
Cleans DOI and page numbers in RIS and TXT files for bibliographic references' deduplication

- DOI fields (`DO`) by adding `https://doi.org/` if missing
- Decoding of encoded characters (e.g., `%28` → `(`, `%29` → `)`)
- Page number formats (`SP`), e.g., converts `123-8` into `123–128`

## 🔧 Features

- Easy file selection via GUI
- Automatically saves a cleaned version next to the original file
- Standalone `.exe` available (no Python installation needed)

## 📦 Installation

### Option 1: Run as `.exe`

1. [Download deduplication-helper-installer.exe](https://constoria.ch/deduplication-helper)

### Option 2: Run the Python script

```bash
python gui_clean_ris_installer.py
