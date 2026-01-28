from .base import BaseValidator
from data_check_tool.utils.text import normalize


class NWCValidator(BaseValidator):
    def validate(self, row):
        status = normalize(row.get("status"))

        if status in ("", "valid"):
            return "VALID", ""

        if status == "a":
            return "INVALID", "Retired lead"

        if status == "!":
            return "INVALID", "Suspicious lead"

        if status in ("r", "no info", "no company match"):
            return "RECHECK", "Missing or unmatched profile"

        return "INVALID", f"Unsupported status value: {status}"