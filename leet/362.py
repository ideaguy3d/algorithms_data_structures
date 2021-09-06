import bisect


class HitCounter1:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = []

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        bisect.insort(self.hits, timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        return bisect.bisect_right(self.hits, timestamp) - bisect.bisect_right(self.hits, max(0, timestamp - 300))




# end
