import os

def simulate_file_deletion(filename):
    try:
        os.remove(filename)
        print(f"File '{filename}' has been deleted (but not securely).")
    except FileNotFoundError:
        print(f"File '{filename}' not found for deletion.")

def simulate_file_recovery(log=None):
    print("Scanning current directory for residual content...\n", file=log)
    for root, dirs, files in os.walk("."):
        for name in files:
            if name.endswith(".log") or name.endswith(".tmp") or name.startswith("~"):
                path = os.path.join(root, name)
                try:
                    with open(path, 'r', errors='ignore') as f:
                        content = f.read()
                        if "Password" in content or "CreditCard" in content:
                            print(f"Potential data leakage found in: {path}", file=log)
                            print(f"Leaked content: {content[:100]}...\n", file=log)
                except Exception:
                    continue
    print("Recovery scan complete.\n", file=log)

def simulate_ssd_trim(filename, log=None):
    """Simulates TRIM command by zeroing file contents before deletion"""
    if os.path.exists(filename):
        with open(filename, 'r+b') as f:
            length = f.seek(0, os.SEEK_END)
            f.seek(0)
            f.write(b'\x00' * length)
        os.remove(filename)
        print(f"Simulated TRIM: zeroed and deleted '{filename}'", file=log)
    else:
        print(f"File '{filename}' not found for TRIM simulation.", file=log)
