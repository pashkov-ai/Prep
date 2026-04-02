import heapq


class EventManager:

    def __init__(self, events: list[list[int]]):
        # O(N log N) - time, O(N) - space
        self.event_map = {}  # matches id to priority, tracks actual state
        self.heap = []
        for (eid, ep) in events:
            self.event_map[eid] = ep
            heapq.heappush(self.heap, (-ep, eid))  # heapify will take O(N) !

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        # O(log N) - time, O(U) - space
        self.event_map[eventId] = newPriority
        heapq.heappush(self.heap, (-newPriority, eventId))

    def pollHighest(self) -> int:
        # O(log N) - time
        if len(self.event_map) == 0:
            return -1

        while True:
            event_priority, event_id = heapq.heappop(self.heap)
            event_priority = -event_priority
            if event_id in self.event_map and self.event_map[event_id] == event_priority:
                self.event_map.pop(event_id)
                return event_id

# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()