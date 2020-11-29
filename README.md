# mopdfs

Merge pdf files and make them searchable with Python.

# Requirements

- MacOS: ``brew install ocrmypdf tesseract-lang``
- Ubuntu: ``sudo apt-get install -y ocrmypdf tesseract-ocr-all``

# Install

```bash
git clone https://github.com/moozeq/mopdfs
cd mopdfs
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

Merged and searchable pdfs will be stored in ``merged_ocr.pdf`` file.