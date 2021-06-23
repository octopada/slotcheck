class SlotChecker:
    def __init__(self):
        self.last = set()

    def check_slots(self, new):
        closed = self.last - new
        opened = new - self.last
        self.last = new
        return {
            "closed": closed,
            "opened": opened
        }
