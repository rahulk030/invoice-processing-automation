import unittest
from datetime import date
from decimal import Decimal
from pathlib import Path

from invoice_processor.models import Invoice
from invoice_processor.validation import validate_invoice


class ValidationTests(unittest.TestCase):
    def make_invoice(self, total: str) -> Invoice:
        return Invoice(
            invoice_number="INV-1",
            vendor="Example Vendor",
            invoice_date=date(2026, 7, 12),
            subtotal=Decimal("100.00"),
            tax=Decimal("13.00"),
            total=Decimal(total),
            source_file=Path("sample.docx"),
        )

    def test_accepts_a_balanced_invoice(self):
        self.assertEqual(validate_invoice(self.make_invoice("113.00")), [])

    def test_flags_a_total_mismatch(self):
        issues = validate_invoice(self.make_invoice("115.00"))
        self.assertEqual(len(issues), 1)
        self.assertIn("$2.00", issues[0].message)


if __name__ == "__main__":
    unittest.main()
