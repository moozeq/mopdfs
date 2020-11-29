# mopdfs

Merge pdf files and make them searchable with OCR.

# Requirements

To OCR languages other than ``eng``:

- MacOS: ``brew install python3 tesseract-lang``
- Ubuntu: ``sudo apt-get install -y python3 tesseract-ocr-all``

# Install

```bash
git clone https://github.com/moozeq/mopdfs
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

# Run

```bash
./mopdfs.py [list of pfds files to be merged] -l <language> -o <output file>
```

List of available languages can be checked with ``tesseract --list-langs``.

# Example

```bash
./mopdfs.py demo/1.pdf demo/2.pdf -l eng -o merged_ocr.pdf
```

Merged and OCRed pdfs will be stored in ``merged_ocr.pdf`` file.