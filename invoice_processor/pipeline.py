from pathlib import Path

from .models import Invoice, ProcessingIssue
from .parser import InvoiceParseError, parse_invoice
from .report import write_excel_report
from .validation import validate_invoice


def process_directory(input_dir: Path, output_path: Path) -> tuple[list[Invoice], list[ProcessingIssue]]:
    if not input_dir.is_dir():
        raise FileNotFoundError(f"Input directory does not exist: {input_dir}")

    invoices = []
    issues = []
    for path in sorted(input_dir.glob("*.docx")):
        try:
            invoice = parse_invoice(path)
            invoices.append(invoice)
            issues.extend(validate_invoice(invoice))
        except (InvoiceParseError, OSError) as exc:
            issues.append(ProcessingIssue(path, str(exc)))

    write_excel_report(invoices, issues, output_path)
    return invoices, issues
