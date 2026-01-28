from .base import BaseValidator
from data_check_tool.utils.text import normalize

LEVEL_KEYWORDS = {
    "c-level": ["ceo", "cto", "cmo", "cfo", "chief"],
    "director+": ["director", "head", "vp", "vice president"],
}

class TitleValidator(BaseValidator):
    def validate(self, row):
        title = normalize(row.get("title"))
        req = normalize(row.get("req"))

        if not title:
            return "INVALID", "Missing title"

        if not req:
            return "INVALID", "Missing requirements"

        # Functional keyword check
        req_tokens = [t for t in req.split() if t]
        if not any(token in title for token in req_tokens):
            return "INVALID", "Title does not contain required keywords"

        # Infer required seniority from req
        required_levels = []

        for level, keywords in LEVEL_KEYWORDS.items():
            if any(k in req for k in keywords):
                required_levels.extend(keywords)

        # If req specifies seniority → enforce it
        if required_levels:
            if not any(level in title for level in required_levels):
                return "INVALID", "Title does not match required seniority level"
        else:
            # If req does not specify level → title must still be senior enough
            if not any(
                level in title
                for keywords in LEVEL_KEYWORDS.values()
                for level in keywords
            ):
                return "INVALID", "Title does not indicate required seniority level"

        return "VALID", ""