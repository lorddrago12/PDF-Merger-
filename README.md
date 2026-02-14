# PDF Merger

A simple Python script to merge all PDF files in the current directory into a single combined PDF.

## Requirements

- Python 3.x
- PyPDF2 library

## Installation

Install the required dependency:

```bash
pip install PyPDF2
```

## Usage

1. Place the `pdfMerger.py` script in the directory containing the PDF files you want to merge
2. Run the script:

```bash
python pdfMerger.py
```

3. The script will create a file named `combinedPDF.pdf` in the same directory containing all the merged PDFs

## How It Works

The script automatically:
- Scans the current directory for all files ending in `.pdf`
- Merges them together in the order they're found
- Outputs a single combined PDF file

## Customization

You can change the output filename by modifying this line in the script:

```python
merger.write("combinedPDF.pdf")  # Change "combinedPDF.pdf" to your desired name
```

## Note

The script merges PDFs in the order returned by `os.listdir()`, which may not be alphabetical. If you need a specific order, you may want to sort the file list before merging.
