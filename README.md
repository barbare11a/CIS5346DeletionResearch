# CIS5346DeletionResearch
Python project for Research Paper Final on The Risks of File Deletion and Data Persistence in Storage Systems.

Deletion Workflow example in workflow.py

This program creates a sensitive file, deletes it using regular file system operations, and attempts to recover it. It also simulates an SSD's TRIM behavior by zeroing the file contents before deletion, mimicking the drive’s internal garbage collection process.

This simulated example demonstrates that regular deletion (os.remove) does not securely erase the file.
- Zeroing the content before deletion reduces, but does not eliminate the chance of recovery. This is similar to what SSDs attempt internally.
- Even after deletion, sensitive data might be recovered from logs, cache, or unallocated space if not properly sanitized.
A full log of the simulation is saved to scan_log.txt, providing a record of what can and cannot be recovered.
