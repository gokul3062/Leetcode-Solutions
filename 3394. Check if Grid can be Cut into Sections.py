'''
Question:

You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles, where rectangles[i] is in the form [startx, starty, endx, endy], representing a rectangle on the grid. Each rectangle is defined as follows:

(startx, starty): The bottom-left corner of the rectangle.
(endx, endy): The top-right corner of the rectangle.
Note that the rectangles do not overlap. Your task is to determine if it is possible to make either two horizontal or two vertical cuts on the grid such that:

Each of the three resulting sections formed by the cuts contains at least one rectangle.
Every rectangle belongs to exactly one section.
Return true if such cuts can be made; otherwise, return false.

Example 1:

Input: n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]

Output: true

Solution:
'''

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        #If there is more than 2 nonOverlapping Points in horizontal or vertical view then it can be divided into 3 valid cuts
        def nonOverlap(rectangle):
            nonOverlap = [rectangle[0]]
            for i in range(1, len(rectangle)):
                prevS, prevE = nonOverlap[-1]
                currS, currE = rectangle[i]

                if prevE > currS:
                    nonOverlap[-1] = [prevS, max(prevE, currE)]
                else:
                    nonOverlap.append(rectangle[i])

                if len(nonOverlap) == 3:
                    return nonOverlap

            return nonOverlap

        horizontal = []
        vertical = []

        for sx, sy, ex, ey in rectangles:
            horizontal.append([sx, ex])
            vertical.append([sy, ey])

      
        horizontal = nonOverlap(sorted(horizontal))
        vertical = nonOverlap(sorted(vertical))
        
        return len(horizontal) == 3 or len(vertical) == 3
