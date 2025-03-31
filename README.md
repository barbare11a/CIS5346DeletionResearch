# CIS5346DeletionResearch
Python project for Research Paper Final on The Risks of File Deletion and Data Persistence in Storage Systems.

This simulated example demonstrates that regular deletion (os.remove) does not securely erase the file.
- Zeroing the content before deletion reduces, but does not eliminate the chance of recovery. This is similar to what SSDs attempt internally.
- Even after deletion, sensitive data might be recovered from logs, cache, or unallocated space if not properly sanitized.
A full log of the simulation is saved to scan_log.txt, providing a record of what can and cannot be recovered.
