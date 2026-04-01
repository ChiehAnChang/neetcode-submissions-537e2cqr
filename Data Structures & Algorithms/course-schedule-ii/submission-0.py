class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # This question we can use an cycle detection algorithm where we basically want to make sure there is no cycle pre-requisites between each of the courses.

        # Step 1:
        # We want to create an adjacent list so that we can run cycle detection algorith (i.e., ) dfs on the graph structure.

        g = {i : [] for i in range(numCourses)}

        # Step 2:
        # Add preprequisites to each course in the graph g
        for each_p in prerequisites:
            # course, preprequisites
            c, p = tuple(each_p)
            g[c].append(p)

        # Step 3:
        # Create a storage to store some intermdiate result

        visiting = set()
        visited = set()
        results = []

        for each_course in g:

            if not self.dfs(g, each_course, visiting, visited, results):
                return []

        return results

    def dfs(self, g, course, visiting, visited, results):

        # Already be detected
        if course in visited:
            return True

        # Cycle
        elif course in visiting:
            return False

        else:

            visiting.add(course)

            for each_p in g[course]:

                if not self.dfs(g, each_p, visiting, visited, results):
                    return False

            visiting.remove(course)

            visited.add(course)

            results.append(course)

            return True


