class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        count =0 
        seats.sort()
        students.sort()

        for i in range(len(seats)):
            while students[i] != seats[i]:
                if students[i]==seats[i]: continue
                elif students[i]>seats[i]:
                    students[i] -= 1
                    count += 1
                else:
                    students[i]+= 1
                    count += 1 
        return count