import heapq

n, m = map(int, input().split())
processing_times = list(map(int, input().split()))

# Create a priority queue of threads and their completion times, initialized with 0 completion time
pq = [(0, i) for i in range(n)] #izveidos prioritātes rindu ar pavedieniem un to izpildes laikus 
heapq.heapify(pq)

for i in range(m):
    completion_time, thread_idx = heapq.heappop(pq) #izņemt padevienu ar mazāko izpildas laiku no prioritātes rindas

    start_time = completion_time #uzdot pavedienam tagatējo uzdevumu
    end_time = start_time + processing_times[i]

    print(thread_idx, start_time) #attēlot piesšķirto pavedienu un sākuma laiku tagatējam uzdevumam

    heapq.heappush(pq, (end_time, thread_idx)) #attēlo uzdevuma izpildes laiku no katra pavediena un pievienot to atpakaļ prioritātes rindai
