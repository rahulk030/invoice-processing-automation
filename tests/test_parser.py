import unittest
from datetime import date
from decimal import Decimal
from pathlib import Path

from invoice_processor.parser import InvoiceParseError, parse_invoice_text


VALID_INVOICE = """
Invoice Number: INV-1042
Vendor: North Shore Office Supply
Invoice Date: 2026-07-12
Subtotal: $245.00
Tax: $31.85
Total: $276.85
"""


class ParserTests(unittest.TestCase):
    def test_parses_a_complete_invoice(self):
        invoice = parse_invoice_text(VALID_INVOICE, Path("sample.docx"))
        self.assertEqual(invoice.invoice_number, "INV-1042")
        self.assertEqual(invoice.vendor, "North Shore Office Supply")
        self.assertEqual(invoice.invoice_date, date(2026, 7, 12))
        self.assertEqual(invoice.total, Decimal("276.85"))

    def test_reports_a_missing_required_field(self):
        with self.assertRaisesRegex(InvoiceParseError, "vendor"):
            parse_invoice_text(VALID_INVOICE.replace("Vendor:", "Company:"), Path("bad.docx"))


if __name__ == "__main__":
    unittest.main()
