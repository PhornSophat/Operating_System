import threading
import time

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.lock = threading.Lock()  # The Mutex for this specific resource

# def transfer(source, target, amount):
#     print(f"Attempting transfer: {source.name} -> {target.name} (${amount})")

def transfer(source, target, amount):
    # Always lock the account with the smaller ID/name first
    first, second = (source, target) if source.name < target.name else (target, source)
    
    with first.lock:
        with second.lock:
            # Critical Section
            source.balance -= amount
            target.balance += amount


    # Acquire the first lock
    with source.lock:
        print(f"  [LOCKED] {source.name} by {threading.current_thread().name}")
        
        # Artificial delay to ensure the other thread grabs the second lock
        time.sleep(1) 
        
        print(f"  [WAITING] {threading.current_thread().name} is trying to lock {target.name}...")
        # Acquire the second lock (This is where the freeze happens)
        with target.lock:
            source.balance -= amount
            target.balance += amount
            print(f"  [SUCCESS] Transfer complete!")

# 1. Initialize Shared Resources
acc1 = Account("Account_1", 1000)
acc2 = Account("Account_2", 1000)

# 2. Define the two threads with circular dependency
# Thread A: Acc1 -> Acc2
t1 = threading.Thread(target=transfer, args=(acc1, acc2, 100), name="Thread-A")

# Thread B: Acc2 -> Acc1 (The reverse order creates the deadlock)
t2 = threading.Thread(target=transfer, args=(acc2, acc1, 50), name="Thread-B")

print("--- Starting Simulation (Expect a freeze) ---")
t1.start()
t2.start()

t1.join()
t2.join()
print("This line will never be reached.")