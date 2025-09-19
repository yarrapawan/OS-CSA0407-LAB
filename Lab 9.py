from multiprocessing import Process, shared_memory

# Child process function
def child(name):
    shm = shared_memory.SharedMemory(name=name)
    # Read first byte
    value = shm.buf[0]
    print("[Child] Read value:", value)
    # Modify the value
    shm.buf[0] = value + 10
    print("[Child] Wrote new value:", shm.buf[0])
    shm.close()

if __name__ == "__main__":
    # Create shared memory of size 1 byte
    shm = shared_memory.SharedMemory(create=True, size=1)
    # Write initial value
    shm.buf[0] = 7
    print("[Parent] Initial value:", shm.buf[0])

    # Start child process
    p = Process(target=child, args=(shm.name,))
    p.start()
    p.join()

    # Read modified value
    print("[Parent] Final value:", shm.buf[0])

    # Clean up
    shm.close()
    shm.unlink()
