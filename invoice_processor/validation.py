from decimal import Decimal

from .models import Invoice, ProcessingIssue


TOLERANCE = Decimal("0.01")


def validate_invoice(invoice: Invoice) -> list[ProcessingIssue]:
    issues = []
    if abs(invoice.difference) > TOLERANCE:
        issues.append(
            ProcessingIssue(
                source_file=invoice.source_file,
                message=(
                    f"Invoice {invoice.invoice_number} total is off by "
                    f"${abs(invoice.difference):.2f}"
                ),
                severity="warning",
            )
        )
    return issues
