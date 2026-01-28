# Data Check Tool

A rule-based data validation tool for lead and company datasets.

## Features
- Sub-status–driven validation logic
- Clear VALID / INVALID / RECHECK outcomes
- Human-readable error messages
- CSV and XLSX input support
- CSV or XLSX output based on file extension
- Designed for scalability and Rust integration

## Installation

```bash
pip install -e .
```

## Usage


```bash
# CSV input, CSV output
data-check --input input.csv --output output.csv

# XLSX input, XLSX output
data-check --input DataCheck_DemoCode.xlsx --output output.xlsx
```

The output format is determined by the output file extension.

## Notes

- VALID rows may have an empty Comment column.
- RECHECK is only produced for the N1: NWC sub-status.