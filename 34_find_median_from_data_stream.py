"""
The median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
"""

import heapq

"""
1- Basic solution:
Insert sort
Time: O(n ^ 2)
Space: O(n)

---

2- Optimized solution:
Using two heap
Time: O(n log n)
Space: O(n)
"""


class MedianFinder:

    def __init__(self):
        self.smaller_half = []  # max heap
        self.greater_half = []  # min heap

    def addNum(self, num: int) -> None:
        if not self.smaller_half:
            heapq.heappush(self.smaller_half, -num)
            return
        mid = -self.smaller_half[0]
        if num > mid:
            heapq.heappush(self.greater_half, num)
        else:
            heapq.heappush(self.smaller_half, -num)

        # Rebalance
        if len(self.greater_half) > len(self.smaller_half):
            heapq.heappush(self.smaller_half, -heapq.heappop(self.greater_half))
        elif len(self.smaller_half) > len(self.greater_half) + 1:
            heapq.heappush(self.greater_half, -heapq.heappop(self.smaller_half))

    def findMedian(self) -> float:
        if not self.smaller_half:
            return
        if len(self.smaller_half) > len(self.greater_half):
            return float(-self.smaller_half[0])
        else:
            return (-self.smaller_half[0] + self.greater_half[0]) / 2


def run_tests():
    obj = MedianFinder()
    obj.addNum(1)
    assert obj.findMedian() == 1

    obj.addNum(2)
    assert obj.findMedian() == 1.5

    obj.addNum(3)
    assert obj.findMedian() == 2

    obj.addNum(-1)
    assert obj.findMedian() == 1.5

    obj.addNum(100)
    assert obj.findMedian() == 2

    print("Done!")


if __name__ == "__main__":
    run_tests()
