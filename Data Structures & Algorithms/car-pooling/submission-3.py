class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        road = [0] * 1001

        for person, start, to in trips:
            for i in range(start, to):

                road[i] = road[i] + person

                if road[i] > capacity:
                    return False
        return True


