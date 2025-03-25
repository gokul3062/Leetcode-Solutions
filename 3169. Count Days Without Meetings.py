'''
Questions:
You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).

Return the count of days when the employee is available for work but no meetings are scheduled.
Note: The meetings may overlap.

Example 1:
Input: days = 10, meetings = [[5,7],[1,3],[9,10]]
Output: 2
Explanation:
There is no meeting scheduled on the 4th and 8th days.

Example 2:
Input: days = 5, meetings = [[2,4],[1,3]]
Output: 1
Explanation:
There is no meeting scheduled on the 5th day.

Solution:
'''

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key=lambda x: x[0])
        nonOverlap = [meetings[0]]
        for i in range(1 , len(meetings)):
            prevS , prevE = nonOverlap[-1]
            currS , currE = meetings[i]

            if prevE >= currS:
                nonOverlap[-1] = [ prevS , max(prevE , currE) ]
            else:
                nonOverlap.append(meetings[i])

        res = 0
        for s , e in nonOverlap:
            res += e - s + 1
        return days - res

