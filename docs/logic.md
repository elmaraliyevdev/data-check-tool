# Data Check Tool – Logic

## Purpose
This tool validates lead and company data row by row based on `sub status` and `req`.
Each row is processed independently and results in `VALID`, `INVALID`, or `RECHECK`,
with a short explanation only when something is wrong.

---

## How Validation Works

1. Load input file (CSV or XLSX).
2. For each row:
   - Read `sub status`.
   - Select the corresponding validation rule.
   - Compare row data with `req` and related fields.
   - Output `Result` and `Comment`.
3. Write results to an output CSV file.

---

## Sub-status Rules

### N/A: Title / PL Summary
- Check that the title contains required functional keywords from `req`.
- Infer required seniority level from `req` (Director, Head, VP, C-level).
- If `req` does not specify level, the title must still indicate a senior role.

**Result:**
- `VALID` if keywords and level match.
- `INVALID` with a clear reason if not.

---

### N/A: Other (auto)
- Company name must exist.
- Industry must exist.
- At least one lead identifier must exist (email or prooflink).

**Result:**
- `VALID` if basic company and lead data are present.
- `INVALID` if critical data is missing.

---

### N/A: Prooflink
- Valid if prooflink contains:
  - `linkedin.com/in/`, or
  - `zoominfo.com/p/`, or
  - an official domain matching the corporate email.

**Result:**
- `VALID` if any condition matches.
- `INVALID` otherwise.

---

### N1: NWC
- Empty or `valid` → `VALID`
- `a` → `INVALID` (retired lead)
- `!` → `INVALID` (suspicious lead)
- `r`, `no info`, `no company match` → `RECHECK`
- Any other value → `INVALID`

`RECHECK` is produced only for this sub-status.

---

## Result and Comment
- `VALID`: Data is correct. Comment is empty.
- `INVALID`: Data is incorrect. Comment explains the issue.
- `RECHECK`: Manual review needed. Comment explains why.

---

## Large Files and Location Checks
For large datasets (50–70k rows) or country checks based on region-only data:
- Process data in chunks.
- Normalize and cache region-to-country mappings.
- Reuse computed mappings to reduce repeated work.