import pprint
# Python program to find maximal Bipartite matching.

AVAILABLE_DATES = [5, 6, 7, 8, 9, 10]
NOTE = {'Hila': [6],
        'Yana': [5],
        'Anat': [5,7,8],
        'Lilach': [6,8],
        'Moran': [],
        'Meital': [10],
        }

def create_graph():
    total_people = len(NOTE)
    total_available_dates = len(AVAILABLE_DATES)
    graph = [[0 for i in range(total_people)] for j in range(total_available_dates)]

    date2idx = {}
    for i, date in enumerate(AVAILABLE_DATES):
        date2idx[AVAILABLE_DATES[i]] = i

    for worker_idx, worker in enumerate(NOTE):
        # worker_idx = 0; worker = list(NOTE.keys())[0]
        # print(f'worker_idx = {worker_idx} worker = {worker}')
        aval_date_per_worker = NOTE[worker]
        for date in aval_date_per_worker:
            # print(f'worker_idx = {worker_idx}, date = {date}, date2idx[date] = {date2idx[date]}')
            graph[date2idx[date]][worker_idx] = 1

    # pprint.pprint(graph)
    return graph

bpGraph = create_graph()
##
# bpGraph = [[0, 1, 1, 0, 0, 0],
#            [1, 0, 0, 1, 0, 0],
#            [0, 0, 1, 0, 0, 0],
#            [0, 0, 1, 1, 0, 0],
#            [0, 0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0, 1]]
##
class GFG:
    def __init__(self, graph):
        # residual graph
        self.graph = graph
        self.ppl = len(graph)
        self.jobs = len(graph[0])
        self.res = dict()

    # A DFS based recursive function that returns true if a matching for vertex u is possible
    def bpm(self, u, matchR, seen):

        # Try every job one by one
        for v in range(self.jobs):

            # If applicant u is interested in job v and v is not seen
            if self.graph[u][v] and seen[v] == False:

                # Mark v as visited
                seen[v] = True

                '''If job 'v' is not assigned to an applicant OR previously assigned  applicant for job v (which is
                matchR[v]) has an alternate job available. Since v is marked as visited in the  above line,
                matchR[v] in the following recursive call will not get job 'v' again'''
                if matchR[v] == -1 or self.bpm(matchR[v], matchR, seen):
                    matchR[v] = u
                    self.res[v] = u
                    return True
        return False

    # Returns maximum number of matching
    def maxBPM(self):
        '''An array to keep track of the applicants assigned to jobs. The value of matchR[i] is the applicant
         number assigned to job i, the value -1 indicates nobody is assigned.'''
        matchR = [-1] * self.jobs

        # Count of jobs assigned to applicants
        result = 0
        for i in range(self.ppl):
            # Mark all jobs as not seen for next applicant.
            seen = [False] * self.jobs

            # Find if the applicant 'u' can get a job
            if self.bpm(i, matchR, seen):
                result += 1

        print(matchR)
        return result


##
g = GFG(bpGraph)
print("Maximum number of applicants that can get job is %d " % g.maxBPM())
print(g.res)

for key in g.res:
    key_res = g.res[key]
    print(f" Date: {AVAILABLE_DATES[key]}, who: {list(NOTE.keys())[key_res]}")

# This code is contributed by Neelam Yadav
