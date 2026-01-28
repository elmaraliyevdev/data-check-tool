from .base import BaseValidator
from data_check_tool.utils.text import normalize


class ProofLinkValidator(BaseValidator):
    def validate(self, row):
        proof = normalize(row.get("prooflink"))
        email = normalize(row.get("email"))

        if "linkedin.com/in/" in proof or "zoominfo.com/p/" in proof:
            return "VALID", ""

        if "@" in email:
            domain = email.split("@")[-1]
            if domain and domain in proof:
                return "VALID", ""

        return "INVALID", "Invalid or missing prooflink"