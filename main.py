import os

ENTRY = "The 400-metre queue: athletes stand in line for four hours; gold goes to whoever complains least and still misses the bus."

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
