from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal
from pathlib import Path


@dataclass(frozen=True)
class Invoice:
    invoice_number: str
    vendor: str
    invoice_date: date
    subtotal: Decimal
    tax: Decimal
    total: Decimal
    source_file: Path

    @property
    def calculated_total(self) -> Decimal:
        return self.subtotal + self.tax

    @property
    def difference(self) -> Decimal:
        return self.total - self.calculated_total


@dataclass(frozen=True)
class ProcessingIssue:
    source_file: Path
    message: str
    severity: str = field(default="error")
