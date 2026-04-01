class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # ... (Your original comments retained) ...
        
        # Step 1: Create adjancent list
        # FIXED: The original dict comprehension was creating map of {index: pair}, 
        # we need {course: [list of dependencies]}. 
        g = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            g[crs].append(pre)
        
        # FIXED: Moved 'visited' set OUTSIDE so it is shared across all recursive calls.
        visiting = set() 

        # Step 2: run dfs on each course
        for each_course in g:
            # FIXED: Pass 'visiting' set into the function
            if not self.dfs(each_course, g, visiting): 
                return False
        return True

    # FIXED: Added 'visiting' as a parameter to the function definition
    def dfs(self, each_course, g, visiting):
        
        # FIXED: Cycle Detection Check moved to the top (Standard DFS)
        # If we see a node that is currently in our path, it's a cycle.
        if each_course in visiting:
            return False

        if not g[each_course]:
            return True

        # check dependency
        # visited = set() <--- DELETED (This was erasing memory every step)
        
        visiting.add(each_course) # Add CURRENT node to path

        for each_dependency in g[each_course]:
            # FIXED: Simplified the loop. 
            # We don't need to check "if in visited" here, because the 
            # recursive call checks it at the very top (lines 26-27).
            if not self.dfs(each_dependency, g, visiting):
                return False
                
        visiting.remove(each_course) # Remove CURRENT node from path (Backtrack)
        
        g[each_course] = [] # Optimization (Memoization)
        return True