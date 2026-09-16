from functions.get_file_content import get_file_content

result01 = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result01)}")
print(f"lorem.txt truncated: {'truncated' in result01}")
print(get_file_content("calculator", "main.py"))
print(get_file_content("calculator", "pkg/calculator.py"))
print(get_file_content("calculator", "/bin/cat"))
print(get_file_content("calculator", "pkg/does_not_exist.py"))

"""
testcases: list[tuple] = [
("calculator", "main.py"),
("calculator", "pkg/calculator.py"),
("calculator", "/bin/cat"), #(this should return an error string)
("calculator", "pkg/does_not_exist.py") #(this should return an error string)
]
for case in testcases:
    result = get_file_content(case[0], case[1])
    if "Error: File not found" in result or "Error: Cannot read" in result:
        print(result) 
    else:
       print(f"{case[1]} length: {len(result)}")
       print(f"{case[1]} truncated: {'truncated' in result}")
"""