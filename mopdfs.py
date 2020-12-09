#!/usr/bin/env python3
import argparse
import subprocess


def merge_jpgs(jpgs: list, output_file: str):
    from fpdf import FPDF

    pdf = FPDF()

    for image in jpgs:
        pdf.add_page()
        pdf.image(image,0,0,210,297)
    pdf.output(output_file, "F")


def merge_pdfs(pdfs: list, output_file: str):
    jpgs = {
        file for file in pdfs if file.lower().endswith('jpg')
    }
    merge_jpgs(jpgs, '__jpgs.pdf')
    
    pdfs = set(pdfs) - jpgs
    pdfs.add('__jpgs.pdf')

    from PyPDF2 import PdfFileMerger

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write(output_file)
    merger.close()


def ocr_pdf(pdf: str, output_file: str, /, *, lang: str = 'eng'):
    cmd = f'ocrmypdf {pdf} {output_file} -l {lang} --force-ocr'
    subprocess.run(cmd.split())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge pdf files and make them searchable with OCR')
    parser.add_argument('files', nargs='+', help='List of files to merge and OCR')
    parser.add_argument('-l', '--lang', type=str, default='eng', help='Files language, check options with "tesseract --list-langs"')
    parser.add_argument('-o', '--out', type=str, default='merged_ocr.pdf', help='Filename for output file')

    args = parser.parse_args()
    merge_pdfs(args.files, f'm_{args.out}')
    ocr_pdf(f'm_{args.out}', args.out, lang=args.lang)
