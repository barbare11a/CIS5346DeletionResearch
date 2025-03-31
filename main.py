import os
import time
from utils import simulate_file_deletion, simulate_file_recovery, simulate_ssd_trim

FILENAME = "secret_data.txt"
SENSITIVE_DATA = "Password=1234abcd; CreditCard=4111-1111-1111-1111"
LOGFILE = "scan_log.txt"

def main():
    with open(LOGFILE, 'w') as log:
        print("[1] Creating sensitive file...", file=log)
        with open(FILENAME, 'w') as f:
            f.write(SENSITIVE_DATA)
        print(f"Sensitive data written to '{FILENAME}'", file=log)

        time.sleep(2)

        print("\n[2] Simulating SSD with TRIM (zeroing content)...", file=log)
        simulate_ssd_trim(FILENAME, log)

        time.sleep(2)

        print("\n[3] Attempting file recovery...", file=log)
        simulate_file_recovery(log)

    print(f"Scan completed. Check '{LOGFILE}' for results.")

if __name__ == "__main__":
    main()
