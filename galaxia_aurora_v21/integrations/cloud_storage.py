from typing import Dict, Any

class CloudStorage:
    def __init__(self, provider: str):
        self.provider = provider
        self.data: Dict[str, Any] = {}

    def save(self, key: str, value: Any):
        self.data[key] = value
        print(f"[{self.provider}] Saved {key}.")

    def load(self, key: str) -> Any:
        return self.data.get(key)

    def sync(self):
        print(f"[{self.provider}] Data synchronized. Total keys: {len(self.data)}.")