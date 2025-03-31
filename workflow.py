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

