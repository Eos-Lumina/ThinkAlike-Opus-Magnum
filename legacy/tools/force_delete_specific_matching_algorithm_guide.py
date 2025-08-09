import os

TARGET = r"c:\Users\w_eed\OneDrive\Desktop\ThinkAlike\ThinkAlike\ThinkAlike\docs\autumn_leaves\archive\matching_algorithm_guide.md"

try:
    if os.path.exists(TARGET):
        os.remove(TARGET)
        print(f"Deleted: {TARGET}")
    else:
        print(f"Not found (already deleted): {TARGET}")
except Exception as e:
    print(f"Error deleting {TARGET}: {e}")
