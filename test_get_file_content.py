from functions.get_file_content import get_file_content

'''print("\n" +
    "Result for current directory:" + "\n" +
      get_files_info("calculator", ".") + "\n\n" +
      "Result for 'pkg' directory:" + "\n" +
      get_files_info("calculator", "pkg") + "\n\n" +
      "Result for '/bin' directory:" + "\n" +
      get_files_info("calculator", "/bin") + "\n\n" +
      "Result for '../' directory:" + "\n" + 
      get_files_info("calculator", "../"))
      '''
result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")
print()