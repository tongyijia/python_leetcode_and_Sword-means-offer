class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(cost) > sum(gas): return -1

        total_gas = 0
        current_gas = 0
        start_station = 0
        for i in range(len(gas)):
            total_gas  += gas[i] - cost[i]
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                start_station = i + 1
                current_gas = 0
        return start_station if total_gas >= 0 else -1
