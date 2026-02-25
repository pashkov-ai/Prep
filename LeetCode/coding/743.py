import heapq
import math
from dataclasses import dataclass, field

@dataclass(frozen=True)
class OutgoingEdge:
    node: int
    weight: int

@dataclass(frozen=True, order=True)
class DistanceToNodeFromK:
    node: int = field(compare=False)
    distance: float

class MinHeap:

    def __init__(self):
        self.heap = [] # O(N) - space

    def __len__(self) -> int:
        return len(self.heap)

    def push(self, elem):
        # O(log N) - time
        heapq.heappush(self.heap, elem)

    def pop(self):
        # O(log N) - time
        return heapq.heappop(self.heap)


class SolutionDijkstra:
    @staticmethod
    def dijkstra(adjacent_list: dict[int, list[OutgoingEdge]], source: int) -> dict[int, float]:
        # O((V + E) log V) - time, O(V + E) - space
        # up-to-date min pathes from source node used in Dijkstra
        min_distances_from_source = {i + 1: math.inf for i in range(len(adjacent_list))} # O(V)- time,space
        min_distances_from_source[source] = 0
        pq = MinHeap() # O(V + E) - space
        pq.push(DistanceToNodeFromK(source, 0))
        # O((V + E) log V) - time
        while pq: # O(V) - time
            dist_to_node = pq.pop() # O(log [V + E]) ~ O(log V) - time

            # already min
            if dist_to_node.distance > min_distances_from_source[dist_to_node.node]:
                continue

            # explore adj nodes
            for out_edge in adjacent_list[dist_to_node.node]: # O(E)
                new_distance = dist_to_node.distance + out_edge.weight
                if new_distance < min_distances_from_source[out_edge.node]:
                    min_distances_from_source[out_edge.node] = new_distance
                    pq.push(DistanceToNodeFromK(out_edge.node, new_distance)) # O(log V) - time
        return min_distances_from_source

    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # V - nodes, E - edges
        # # O((V + E) log V) - time, O(V + E) - space
        adj_list = {i + 1: list() for i in range(n)} # O(V + E) - space
        for (u, v, w) in times: # O(E) - time
            adj_list[u].append(OutgoingEdge(v, w))

        min_distances_from_k = self.dijkstra(adj_list, k) # O((V + E) log V) - time, O(V + E) - space
        min_time_node = max(min_distances_from_k, key=lambda i: min_distances_from_k[i]) # O(V) - time
        min_time = min_distances_from_k[min_time_node]
        return min_time if min_time < math.inf else -1

