class RecentCounter:
    def __init__(self):
        self.counter = []
        
    def ping(self, t: int) -> int:
        self.counter.append(t)
        count = 0
        for x in self.counter:
            if x >= t - 3000 and x <= t:
                count += 1
        return count

        