from .base import BaseValidator
from data_check_tool.utils.text import normalize


class NWCValidator(BaseValidator):
    def validate(self, row):
        status = normalize(row.get("status"))

        if not status or status == "valid":
            return "VALID", ""

        if status == "a":
            return "INVALID", "Retired lead"

        if status == "!":
            return "INVALID", "Suspicious lead"

        if status == "r":
            return "RECHECK", "Retired status requires recheck"

        if status == "no info":
            return "RECHECK", "No information available"

        if status == "no company match":
            return "RECHECK", "No company match"

        return "INVALID", f"Unsupported status value: {status}"