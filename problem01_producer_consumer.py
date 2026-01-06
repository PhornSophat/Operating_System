import threading
import time
import random

# Shared buffer
BUFFER_SIZE = 100
buffer = []

# Semaphores
empty = threading.Semaphore(BUFFER_SIZE)  # empty slots
full = threading.Semaphore(0)  # filled slots
mutex = threading.Semaphore(1)  # mutual exclusion


def producer(pid):
    """Producer function that produces pairs of items."""
    while True:
        # Produce a pair
        p1 = f"P{pid}-1"
        p2 = f"P{pid}-2"
        
        # Wait for two empty slots
        empty.acquire()
        empty.acquire()
        
        # Enter critical section
        mutex.acquire()
        buffer.append(p1)
        buffer.append(p2)
        print(f"Producer {pid} produced {p1}, {p2}")
        
        # Leave critical section
        mutex.release()
        
        # Signal two full slots
        full.release()
        full.release()
        
        time.sleep(random.uniform(0.5, 1.5))


def consumer():
    """Consumer function that consumes pairs of items."""
    while True:
        # Wait for two full slots
        full.acquire()
        full.acquire()
        
        # Enter critical section
        mutex.acquire()
        p1 = buffer.pop(0)
        p2 = buffer.pop(0)
        print(f"Consumer consumed {p1}, {p2}")
        
        # Leave critical section
        mutex.release()
        
        # Signal two empty slots
        empty.release()
        empty.release()
        
        time.sleep(random.uniform(1, 2))


# Create threads
producers = []
for i in range(3):  # 3 producers
    t = threading.Thread(target=producer, args=(i,))
    producers.append(t)
    t.start()

consumer_thread = threading.Thread(target=consumer)
consumer_thread.start()