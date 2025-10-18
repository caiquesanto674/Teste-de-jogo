import datetime
import random
from typing import Dict, Any, List

class AIProtocol:
    def __init__(self):
        self.version = 1.0
        self.log: List[str] = []

    def analyze_context(self, context: Dict[str, Any]):
        if context.get("threat"):
            self.log.append(f"{datetime.datetime.now()}: Threat detected. Preparing defenses.")
        if context.get("market_crash"):
            self.log.append(f"{datetime.datetime.now()}: Market crash detected. Adjusting prices.")
        if random.random() > 0.9:
            self.log.append(f"{datetime.datetime.now()}: New narrative event triggered.")

    def show_log(self):
        print("--- AI Log ---")
        for entry in self.log[-5:]:
            print(entry)