#
# @lc app=leetcode id=871 lang=python3
#
# [871] Minimum Number of Refueling Stops
#

# @lc code=start
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, 0])
        if not len(stations):
            return 0 if startFuel >= target else -1
        fuelLeftAtLastStation = [0] * 15
        fuelLeftAtLastStation[0] = startFuel
        minStopSoFar = 0
        stationsVisited = 0
        prevStationMile = 0
        for mile, fuel in stations:
            gap = mile - prevStationMile
            print(fuelLeftAtLastStation, minStopSoFar, stationsVisited, (mile, fuel), gap)
            for numStopBeforeThisStation in range(stationsVisited, minStopSoFar-1, -1):
                if fuelLeftAtLastStation[numStopBeforeThisStation] < gap:
                    if numStopBeforeThisStation == stationsVisited:
                        return -1
                    minStopSoFar = numStopBeforeThisStation + 1
                    fuelLeftAtLastStation[numStopBeforeThisStation] = 0
                    break
                # can reach this station with numStop 
                if numStopBeforeThisStation == stationsVisited:
                    fuelLeftAtLastStation[stationsVisited + 1] = fuelLeftAtLastStation[stationsVisited] + fuel - gap
                if numStopBeforeThisStation > minStopSoFar:
                    fuelLeftAtLastStation[numStopBeforeThisStation] = max(
                        fuelLeftAtLastStation[numStopBeforeThisStation],
                        fuelLeftAtLastStation[numStopBeforeThisStation - 1] + fuel
                    ) - gap
                else:
                    fuelLeftAtLastStation[numStopBeforeThisStation] -= gap

            prevStationMile = mile
            stationsVisited += 1

        # while numStopToFuelLeft[minStopSoFar] + stations[minStopSoFar][0] < target:
        #     minStopSoFar += 1
        # if minStopSoFar > stationsVisited:
        #     return -1
        return minStopSoFar  

        
# @lc code=end

