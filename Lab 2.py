# File Copying

import os

def copy_file(src, dst):
    # Open source file (read-only)
    fd_src = os.open(src, os.O_RDONLY)

    # Open destination file (write-only, create if not exists, truncate)
    fd_dst = os.open(dst, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)

    while True:
        data = os.read(fd_src, 1024)  # Read 1KB chunks
        if not data:
            break
        os.write(fd_dst, data)  # Write to destination

    os.close(fd_src)
    os.close(fd_dst)
    print(f"Copied content from {src} to {dst}")

if _name_ == "_main_":
    copy_file("source.txt", "destination.txt")