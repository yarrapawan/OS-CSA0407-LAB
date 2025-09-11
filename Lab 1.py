# Process Creation

import os
pid = os.fork()  # create new process

if pid == 0:
    # Child process
    child_pid = os.getpid()
    parent_pid = os.getppid()
    print("Child Process: PID =", child_pid, "PPID =", parent_pid)
elif pid > 0:
    # Parent process
    parent_pid = os.getpid()
    grandparent_pid = os.getppid()
    print("Parent Process: PID =", parent_pid, "PPID =", grandparent_pid)
else:
    print("Fork failed")
    