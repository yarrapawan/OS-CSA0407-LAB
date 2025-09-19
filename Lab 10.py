from multiprocessing import Process, Queue

def child(q_in, q_out):
    # Get value from parent
    num = q_in.get()
    print("[Child] Received:", num, flush=True)
    # Process the number
    new_num = num + 10
    print("[Child] Sending back:", new_num, flush=True)
    # Send result back to parent
    q_out.put(new_num)
if __name__ == "__main__":
    # Two queues: one for sending to child, one for receiving from child
    parent_to_child = Queue()
    child_to_parent = Queue()
    # Start child process
    p = Process(target=child, args=(parent_to_child, child_to_parent))
    p.start()
    # Parent sends a number
    parent_to_child.put(7)
    print("[Parent] Sent: 7", flush=True)
    # Parent waits for result from child
    result = child_to_parent.get()
    print("[Parent] Received:", result, flush=True)
    p.join()
