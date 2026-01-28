import pandas as pd
from pathlib import Path

from data_check_tool.validators.nwc_validator import NWCValidator
from data_check_tool.validators.prooflink_validator import ProofLinkValidator
from data_check_tool.validators.title_validator import TitleValidator
from data_check_tool.validators.auto_validator import AutoValidator
from data_check_tool.utils.text import normalize


VALIDATORS = {
    "nwc": NWCValidator(),
    "prooflink": ProofLinkValidator(),
    "title": TitleValidator(),
    "other": AutoValidator(),
}


def get_validator(sub_status: str):
    sub_status = normalize(sub_status)

    if "nwc" in sub_status:
        return VALIDATORS["nwc"]
    if "prooflink" in sub_status:
        return VALIDATORS["prooflink"]
    if "title" in sub_status:
        return VALIDATORS["title"]

    return VALIDATORS["other"]


def load_dataframe(input_path: str) -> pd.DataFrame:
    path = Path(input_path)
    ext = path.suffix.lower()

    try:
        if ext == ".csv":
            df = pd.read_csv(path, sep=None, engine="python")
        elif ext in (".xlsx", ".xls"):
            df = pd.read_excel(path)
        else:
            raise ValueError(f"Unsupported file type: {ext}")
    except pd.errors.EmptyDataError:
        raise ValueError(f"Input file '{input_path}' is empty or invalid")

    if df.empty:
        raise ValueError(f"Input file '{input_path}' contains no rows")

    return df


def process_file(input_path: str, output_path: str):
    out_path = Path(output_path)
    ext = out_path.suffix.lower()
    df = load_dataframe(input_path)

    if ext not in (".csv", ".xlsx"):
        raise ValueError("Output file must be .csv or .xlsx")

    def process_row(row):
        validator = get_validator(row.get("sub status"))
        result, comment = validator.validate(row)

        # Enforce comment for INVALID / RECHECK
        if result in ("INVALID", "RECHECK") and not comment:
            comment = "Validation failed"

        return result, comment

    results = df.apply(process_row, axis=1)
    df["Result"] = results.apply(lambda x: x[0])
    df["Comment"] = results.apply(lambda x: x[1])

    if ext == ".xlsx":
        df.to_excel(out_path, index=False)
    else:
        df.to_csv(out_path, index=False)