import json
import hmac
import hashlib
import requests
from datetime import datetime, timezone

SIGNING_SECRET = b"hello-there-from-b12"

payload = {
    "action_run_link": "https://github.com/elmaraliyevdev/data-check-tool/actions/runs/21673613871",
    "email": "elmaraliyevdev@gmail.com",
    "name": "Elmar Aliyev",
    "repository_link": "https://github.com/elmaraliyevdev/data-check-tool",
    "resume_link": "https://www.linkedin.com/in/elmaraliyevdev/",
    "timestamp": datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z"),
}

# Canonical JSON
body = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode("utf-8")

# HMAC SHA256
digest = hmac.new(SIGNING_SECRET, body, hashlib.sha256).hexdigest()
headers = {
    "Content-Type": "application/json",
    "X-Signature-256": f"sha256={digest}",
}

response = requests.post("https://b12.io/apply/submission", data=body, headers=headers)
print(response.text)