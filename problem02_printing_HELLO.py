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