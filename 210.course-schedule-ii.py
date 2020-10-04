#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        seen = [False] * numCourses
        courseToPreq = [set() for i in range(numCourses)]
        preqToCourses= [set() for i in range(numCourses)]
        for course, prereq in prerequisites:
            courseToPreq[course].add(prereq)
            preqToCourses[prereq].add(course)

        cycleCheck = [False] * numCourses
        frontier = set([0])
        while len(frontier) > 0:
            newFront = set()
            for course in frontier:
                cycleCheck[course] = True
                for pre in courseToPreq(course):
                    if cycleCheck[pre]:
                        return []
                    newFront.add(pre)
            frontier = newFront
            

        cursor = 0
        while True:
            for course in range(numCourses):
                if seen[course]:
                    continue
                canTake = True
                for prereq in dic[course]:
                    if not seen[prereq]:
                        canTake = False
                        break
                if canTake:
                    result[cursor] = course
                    cursor += 1
                    if cursor >= numCourses:
                        return result
                    seen[course] = True
        
# @lc code=end

