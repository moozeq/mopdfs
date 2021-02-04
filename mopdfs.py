#!/usr/bin/env python3
import argparse
import subprocess
from pathlib import Path
from typing import List


# def merge_jpgs(jpgs: list, output_file: str):
#     from fpdf import FPDF

#     pdf = FPDF()

#     for image in jpgs:
#         pdf.add_page()
#         pdf.image(image,0,0,210,297)
#     pdf.output(output_file, "F")

#     jpgs = {
#         file for file in pdfs if file.lower().endswith('jpg')
#     }
#     merge_jpgs(jpgs, '__jpgs.pdf')
    
#     pdfs = set(pdfs) - jpgs
#     pdfs.add('__jpgs.pdf')


def merge_pdfs(pdfs: list, output_file: str):
    if Path(output_file).exists():
        return

    from PyPDF2 import PdfFileMerger

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write(output_file)
    merger.close()
    print(f'[+] Merged to: {output_file}')


def ocr_pdfs(pdfs: List[str], /, *, lang: str = 'eng') -> List[str]:
    ocred = []
    for pdf in pdfs:
        out = f'ocr_{len(ocred)}.pdf'
        try:
            subprocess.run(['ocrmypdf', pdf, out, '-l', lang, '--force-ocr'])
            ocred.append(out)
            print(f'[+] OCRed: {pdf} -> {out}, ({len(ocred)}/{len(pdfs)})')
        except:
            print(f'[-] OCR failed: {pdf}')
        
    return ocred


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge pdf files and make them searchable with OCR')
    parser.add_argument('files', nargs='+', help='List of files to merge and OCR')
    parser.add_argument('-l', '--lang', type=str, default='eng', help='Files language, check options with "tesseract --list-langs"')
    parser.add_argument('-o', '--out', type=str, default='merged_ocr.pdf', help='Filename for output file')

    args = parser.parse_args()
    ocred = ocr_pdfs(args.files, lang=args.lang)
    merge_pdfs(ocred, args.out)
