from .base import BaseValidator
from data_check_tool.utils.text import normalize


class AutoValidator(BaseValidator):
    def validate(self, row):
        company = normalize(row.get("company"))
        industry = normalize(row.get("industry"))
        email = normalize(row.get("email"))
        prooflink = normalize(row.get("prooflink"))

        if not company or not industry:
            return "INVALID", "Missing company or industry"

        if not email and not prooflink:
            return "INVALID", "Missing contact information"

        return "VALID", ""