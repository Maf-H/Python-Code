from collections import deque
class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        # adds current time to the request queue
        self.requests.append(t)
        # checks the time difference between the first request and current request: 
        # if time span >3000ms discard current request
        print('1:', self.requests)
        while self.requests and self.requests[0] < (t - 3000):
            self.requests.popleft()
            print('2:', self.requests)
        return len(self.requests)
recent_counter = RecentCounter()
recent_counter.ping(1)
recent_counter.ping(100)
recent_counter.ping(3001)
print(recent_counter.ping(3002))      

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# [[],[1],[100],[3001],[3002]] ->[null,1,2,3,4]
