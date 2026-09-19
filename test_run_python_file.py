from functions.run_python_file import run_python_file

print("--- Test 1: Usage Instructions ---") 
print(run_python_file("calculator", "main.py"))

print("\n--- Test 2: Addition ---")
print(run_python_file("calculator", "main.py", ["3 + 5"]))

print("\n--- Test 3: Tests.py ---")
print(run_python_file("calculator", "tests.py"))

print("\n--- Test 4: Path Traversal (Error) ---")
print(run_python_file("calculator", "../main.py"))

print("\n--- Test 5: Nonexistent File (Error) ---")
print(run_python_file("calculator", "nonexistent.py"))

print("\n--- Test 6: Wrong Extension (Error) ---")
print(run_python_file("calculator", "lorem.txt"))
