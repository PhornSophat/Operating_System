# <center> Semaphore

## lecturer : HENG RathPisey 

<br>

### name : PHORN SOPHATH
### id : e20220628

<hr>

#### Problem 1 :

```python
import threading
import time
import random

# ----------------------------
# Shared buffer
# ----------------------------
BUFFER_SIZE = 100
buffer = []

# ----------------------------
# Semaphores
# ----------------------------
empty = threading.Semaphore(BUFFER_SIZE)  # empty slots
full = threading.Semaphore(0)              # filled slots
mutex = threading.Semaphore(1)             # mutual exclusion


# ----------------------------
# Producer function
# ----------------------------
def producer(pid):
    while True:
        # produce a pair
        p1 = f"P{pid}-1"
        p2 = f"P{pid}-2"

        # wait for two empty slots
        empty.acquire()
        empty.acquire()

        # enter critical section
        mutex.acquire()

        buffer.append(p1)
        buffer.append(p2)
        print(f"Producer {pid} produced {p1}, {p2}")

        # leave critical section
        mutex.release()

        # signal two full slots
        full.release()
        full.release()

        time.sleep(random.uniform(0.5, 1.5))


# ----------------------------
# Consumer function
# ----------------------------
def consumer():
    while True:
        # wait for two full slots
        full.acquire()
        full.acquire()

        # enter critical section
        mutex.acquire()

        p1 = buffer.pop(0)
        p2 = buffer.pop(0)
        print(f"Consumer consumed {p1}, {p2}")

        # leave critical section
        mutex.release()

        # signal two empty slots
        empty.release()
        empty.release()

        time.sleep(random.uniform(1, 2))


# ----------------------------
# Create threads
# ----------------------------
producers = []
for i in range(3):  # 3 producers
    t = threading.Thread(target=producer, args=(i,))
    producers.append(t)
    t.start()

consumer_thread = threading.Thread(target=consumer)
consumer_thread.start()

```

#### result :

```
(myprojectDjango) sophat-phorn@Vostro-3520:~/Documents/Year4/OS/Acitvity:_Synchronization&Semaphore/semaphore$ python ./problem01_producer_consumer.py
Producer 0 produced P0-1, P0-2
Producer 1 produced P1-1, P1-2
Producer 2 produced P2-1, P2-2
Consumer consumed P0-1, P0-2
Producer 0 produced P0-1, P0-2
Producer 2 produced P2-1, P2-2
Producer 1 produced P1-1, P1-2
Producer 0 produced P0-1, P0-2
Producer 2 produced P2-1, P2-2
Producer 1 produced P1-1, P1-2
Consumer consumed P1-1, P1-2
Producer 2 produced P2-1, P2-2
Producer 0 produced P0-1, P0-2
Producer 1 produced P1-1, P1-2
Producer 2 produced P2-1, P2-2
Consumer consumed P2-1, P2-2
Producer 0 produced P0-1, P0-2
Producer 1 produced P1-1, P1-2
Producer 2 produced P2-1, P2-2
Producer 0 produced P0-1, P0-2
Producer 1 produced P1-1, P1-2
Consumer consumed P0-1, P0-2
Producer 2 produced P2-1, P2-2
Producer 1 produced P1-1, P1-2
Consumer consumed P1-1, P1-2
Producer 2 produced P2-1, P2-2
Producer 0 produced P0-1, P0-2
Producer 1 produced P1-1, P1-2
Producer 2 produced P2-1, P2-2
Consumer consumed P2-1, P2-2
Producer 0 produced P0-1, P0-2
Producer 1 produced P1-1, P1-2
Producer 2 produced P2-1, P2-2
Producer 0 produced P0-1, P0-2
Producer 1 produced P1-1, P1-2

```

<hr>

#### Problem 2 :

```py
# Problem 2: Printing HELLO using Semaphores
# One-file Python version (for learning purpose)

import threading
import time

# ----------------------------
# Semaphore initialization
# ----------------------------
a = threading.Semaphore(1)   # Process 1 can start
b = threading.Semaphore(0)   # Process 2 waits
c = threading.Semaphore(0)   # Process 3 waits


# ----------------------------
# Process 1: prints H and E
# ----------------------------
def process1():
    a.acquire()          # wait(a)
    print("H", end="")
    time.sleep(0.1)
    print("E", end="")
    b.release()          # signal(b)


# ----------------------------
# Process 2: prints L
# ----------------------------
def process2():
    b.acquire()       # wait(b)
    print("L", end="")
    c.release()          # signal(c)


# ----------------------------
# Process 3: prints O
# ----------------------------
def process3():
    c.acquire() 
    # c.acquire()         # wait(c)
    print("O", end="")


# ----------------------------
# Create and start threads
# ----------------------------
t1 = threading.Thread(target=process1)
t2 = threading.Thread(target=process2)
t3 = threading.Thread(target=process3)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print()  # new line

```


#### result:

```
(myprojectDjango) sophat-phorn@Vostro-3520:~/Documents/Year4/OS/Acitvity:_Synchronization&Semaphore/semaphore$ python ./problem02_printing_HELLO.py
HELO

```


#### link : 
```link 
https://github.com/ChingHoir/Operating_System/tree/Semaphore
```