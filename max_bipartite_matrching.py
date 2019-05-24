# import pandas as pd
import pprint


def preprocess(AVAILABLE_DATES, NOTE):
    AVAILABLE_DATES_set = set(AVAILABLE_DATES)
    for worker in NOTE.keys():
        NOTE[worker] = sorted(list(AVAILABLE_DATES_set - set(NOTE[worker])))
        # print(f"worker: {worker:10} |     {sorted(list(AVAILABLE_DATES_set - set(NOTE[worker])))}")
    return NOTE


def create_graph(AVAILABLE_DATES, NOTE):
    NOTE = preprocess(AVAILABLE_DATES, NOTE)
    # print(f"After Preprocessing: {NOTE}")
    total_people = len(NOTE)
    total_available_dates = len(AVAILABLE_DATES)
    graph = [[0 for _ in range(total_people)] for _ in range(total_available_dates)]

    date2idx = {key: i for (i, key) in enumerate(AVAILABLE_DATES)}

    for worker_idx, worker in enumerate(NOTE):
        # worker_idx = 0; worker = list(NOTE.keys())[0]
        # print(f'worker_idx = {worker_idx} worker = {worker}')
        aval_date_per_worker = NOTE[worker]
        for date in aval_date_per_worker:
            # print(f'worker_idx = {worker_idx}, date = {date}, date2idx[date] = {date2idx[date]}')
            graph[date2idx[date]][worker_idx] = 1

    # pprint.pprint(graph)
    return graph


# bpGraph = create_graph()

#
# bpGraph = [[0, 1, 1, 0, 0, 0],
#            [1, 0, 0, 1, 0, 0],
#            [0, 0, 1, 0, 0, 0],
#            [0, 0, 1, 1, 0, 0],
#            [0, 0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0, 1]]
#
class GFG:
    def __init__(self, graph):
        # residual graph
        self.graph = graph
        self.ppl = len(graph)
        self.jobs = len(graph[0])
        self.res = dict()

    # A DFS based recursive function that returns true if a matching for vertex u is possible
    def bpm(self, u, match_r, seen):

        # Try every job one by one
        for v in range(self.jobs):

            # If applicant u is interested in job v and v is not seen
            if self.graph[u][v] and seen[v] is False:

                # Mark v as visited
                seen[v] = True

                # If job 'v' is not assigned to an applicant OR previously assigned  applicant for job v (which is
                # matchR[v]) has an alternate job available. Since v is marked as visited in the  above line,
                # matchR[v] in the following recursive call will not get job 'v' again
                if match_r[v] == -1 or self.bpm(match_r[v], match_r, seen):
                    match_r[v] = u
                    self.res[v] = u
                    return True
        return False

    # Returns maximum number of matching
    def max_bpm(self):
        """An array to keep track of the applicants assigned to jobs. The value of matchR[i] is the applicant
         number assigned to job i, the value -1 indicates nobody is assigned."""
        match_r = [-1] * self.jobs

        # Count of jobs assigned to applicants
        result = 0
        for i in range(self.ppl):
            # Mark all jobs as not seen for next applicant.
            seen = [False] * self.jobs

            # Find if the applicant 'u' can get a job
            if self.bpm(i, match_r, seen):
                result += 1

        # print(match_r)
        return result


def wrapper(AVAILABLE_DATES, NOTE):
    bpGraph = create_graph(AVAILABLE_DATES, NOTE)
    g = GFG(bpGraph)
    # print("Maximum number of applicants that can get job is %d " % g.maxBPM())
    g.max_bpm()
    # print(g.res)
    people_list = list(NOTE.keys())

    for person in g.res:
        date = g.res[person]
        print(f" Date: {AVAILABLE_DATES[date]:3d} who: {people_list[person]}")
