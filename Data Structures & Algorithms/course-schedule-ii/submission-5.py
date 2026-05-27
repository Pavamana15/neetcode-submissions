class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Store all courses along the current DFS path
        visiting = set()
        Courses = []
        def dfs(crs):
            
            if crs in visiting:
                # Cycle detected
                return False
            if preMap[crs] == []:
                if crs not in Courses:
                    Courses.append(crs)
                print("The courses list are:", Courses)
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            Courses.append(crs)
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
            # else:
            #     Courses.add(c)

        return Courses