"""
Rate Limiter
limit: 5 request per 10 seconds:
"""
import time
from collections import deque


class TokenBucketRateLimiter:
    def __init__(self, refill_seconds: int, capacity: int):
        self.refill_seconds = refill_seconds
        self.capacity = capacity
        self.tokens = capacity
        self.last_refill = time.time()

    def allow_request(self) -> bool:
        now = time.time()
        self.tokens += (now - self.last_refill) * self.refill_seconds / 60
        self.tokens = min(self.tokens, self.capacity)
        self.last_refill = now

        if self.tokens < 1:
            return False
        self.tokens -= 1
        return True


class FixedWindowRateLimiter:
    def __init__(self, window_size_seconds: int, max_request: int):
        self.window_size_seconds = window_size_seconds
        self.max_request = max_request
        self.used_requests = 0
        self.window_start = time.time()

    def allow_request(self) -> bool:
        now = time.time()
        if now - self.window_start >= self.window_size_seconds:
            self.window_start = now
            self.used_requests = 0
        if self.used_requests >= self.max_request:
            return False
        self.used_requests += 1
        return True


class SlidingWindowRateLimiter:
    def __init__(self, window_size_seconds: int, max_request: int):
        self.window_size_seconds = window_size_seconds
        self.max_request = max_request
        self.request_times = deque()

    def allow_request(self) -> bool:
        now = time.time()
        while self.request_times and now - self.request_times[0] >= self.window_size_seconds:
            self.request_times.popleft()
        if len(self.request_times) >= self.max_request:
            return False
        self.request_times.append(now)
        return True


def run_tests():
    all_rate_limiters = [
        TokenBucketRateLimiter(refill_seconds=10, capacity=5),
        FixedWindowRateLimiter(window_size_seconds=10, max_request=5),
        SlidingWindowRateLimiter(window_size_seconds=10, max_request=5)
    ]
    for rate_limiter in all_rate_limiters:
        print(f"Test {rate_limiter.__class__.__name__} ...")
        for i in range(5):
            assert rate_limiter.allow_request(), f"{i=}"

        assert not rate_limiter.allow_request(), "Must limit after 5 request!"
        print("sleep 10 sec")
        time.sleep(10)
        assert rate_limiter.allow_request()

    print("All tests passed.")

if __name__ == "__main__":
    run_tests()
