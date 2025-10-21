import random

class Ticker:
    """Manages and displays the game log of events."""
    def __init__(self):
        self.log = []
    def register(self, txt):
        self.log.append(txt)
    def show(self):
        for l in self.log[-6:]:  # Shows the last events
            print(l)

class World:
    def __init__(self):
        self.events = []
        self.weather = "normal"
        self.crisis = False
    def run_event(self, ticker):
        if random.random() > 0.8:
            self.crisis = True
            evt = "Alien invasion detected!"
            ticker.register(f"[WORLD] {evt} ⚡")
        elif random.random() > 0.7:
            self.weather = "quantum_storm"
            ticker.register(f"[WORLD] Quantum Storm! Effects on energy production.")
        else:
            self.weather = "normal"
            self.crisis = False
