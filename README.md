# CIS5346DeletionResearch
Python project for Research Paper Final on The Risks of File Deletion and Data Persistence in Storage Systems.

Deletion Workflow example: 

# Step 1: Create sensitive data
with open("secret_data.txt", "w") as f:
    f.write("Password=1234abcd; CreditCard=4111-1111-1111-1111")

# Step 2: Simulate TRIM by zeroing file content before deletion
with open("secret_data.txt", 'r+b') as f:
    length = f.seek(0, os.SEEK_END)
    f.seek(0)
    f.write(b'\x00' * length)
os.remove("secret_data.txt")

# Step 3: Attempt recovery by scanning directory


This simulated example demonstrates that regular deletion (os.remove) does not securely erase the file.
- Zeroing the content before deletion reduces, but does not eliminate the chance of recovery. This is similar to what SSDs attempt internally.
- Even after deletion, sensitive data might be recovered from logs, cache, or unallocated space if not properly sanitized.
A full log of the simulation is saved to scan_log.txt, providing a record of what can and cannot be recovered.
