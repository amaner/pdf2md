# PDF to Markdown Converter

A simple Python utility that converts PDF documents to Markdown format.

## Author

Andrew Maner

## Description

This tool extracts text from PDF files and converts it to Markdown format. It uses `pdfplumber` to extract text from each page of the PDF and saves the result to a markdown file.

## Requirements

- Python 3.x
- pdfplumber
- markdownify

## Installation

1. Clone this repository
2. Install the required packages:

```bash
pip install pdfplumber markdownify
```

## Usage

1. Place your PDF file in the project directory
2. Modify the last line in `pdf2md.py` to specify your input PDF and desired output file:

```python
pdf_to_md("your_file.pdf", "output.md")
```

3. Run the script:

```bash
python pdf2md.py
```

## Features

- Extracts text from PDF documents
- Preserves paragraph structure
- Outputs clean Markdown text

## Example

The default configuration converts a file named `atssprop.pdf` to `output.md`.

## Notes

- The output.md file is ignored by git (see .gitignore)
- All PDF files are also excluded from version control
