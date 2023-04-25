import heapq

n, m = map(int, input().split())
processing_times = list(map(int, input().split()))

# Create a priority queue of threads and their completion times, initialized with 0 completion time
pq = [(0, i) for i in range(n)]
heapq.heapify(pq)

for i in range(m):
    # Pop the thread with the smallest completion time from the priority queue
    completion_time, thread_idx = heapq.heappop(pq)

    # Assign the thread to the current job
    start_time = completion_time
    end_time = start_time + processing_times[i]

    # Output the assigned thread and start time of the current job
    print(thread_idx, start_time)

    # Update the completion time of the assigned thread and add it back to the priority queue
    heapq.heappush(pq, (end_time, thread_idx))
