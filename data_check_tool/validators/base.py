from typing import Tuple, Dict, Any


class BaseValidator:
    def validate(self, row: Dict[str, Any]) -> Tuple[str, str]:
        raise NotImplementedError