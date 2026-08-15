import argparse
from pathlib import Path

from .pipeline import process_directory


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Extract Word invoice data and create a reviewed Excel report."
    )
    parser.add_argument("input_dir", type=Path, help="Directory containing .docx invoices")
    parser.add_argument(
        "--output", type=Path, default=Path("invoice-report.xlsx"), help="Excel report path"
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    invoices, issues = process_directory(args.input_dir, args.output)
    print(f"Processed {len(invoices)} invoice(s); found {len(issues)} exception(s).")
    print(f"Report written to {args.output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
