# Invoice Processing Automation

A command-line workflow that reads invoice details from Microsoft Word files, validates the totals, and produces a formatted Excel workbook for review. It turns a repetitive copy-and-paste task into a repeatable process while keeping exceptions visible to a human reviewer.

## What it does

- Scans a folder for `.docx` invoices
- Extracts the invoice number, vendor, date, subtotal, tax, and total
- Reads details from both paragraphs and tables
- Recalculates totals and flags mismatches
- Continues past malformed files and records each problem
- Produces `Invoices`, `Exceptions`, and `Summary` worksheets
- Applies practical spreadsheet formatting, filters, frozen headers, and currency formats

## Stack

Python, pandas, OpenPyXL, python-docx, regular expressions, and unittest.

## Set up

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Generate two safe sample invoices, including one deliberate total mismatch:

```bash
python scripts/generate_sample_invoices.py
```

Process them:

```bash
python -m invoice_processor.cli examples/invoices --output invoice-report.xlsx
```

The report is designed for review, not silent approval: malformed documents and total differences appear on the `Exceptions` worksheet.

## Expected invoice labels

The parser recognizes common labels such as:

```text
Invoice Number: INV-1042
Vendor: North Shore Office Supply
Invoice Date: 2026-07-12
Subtotal: $245.00
Tax: $31.85
Total: $276.85
```

## Tests

```bash
python -m unittest discover -s tests -v
```

## Design notes

- `parser.py` owns document extraction and field parsing.
- `validation.py` contains review rules without file-system concerns.
- `report.py` is responsible only for workbook output and formatting.
- `pipeline.py` coordinates files and records failures without stopping the entire batch.

This separation keeps the automation easy to extend when a supplier uses a different invoice layout.
