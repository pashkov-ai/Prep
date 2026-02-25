class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:


        def getTripsForTime(time_given):
            return sum(time_given // t for t in time)

        min_bus_time = min(time)
        left = 1
        right = min_bus_time * totalTrips

        while left < right:
            midtime = (left + right) // 2
            trips = getTripsForTime(midtime)
            if trips >= totalTrips:
                right = midtime
            else:
                left = midtime + 1

        return left