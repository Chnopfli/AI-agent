from functions.get_files_info import get_files_info

print("\n" +
    "Result for current directory:" + "\n" +
      get_files_info("calculator", ".") + "\n\n" +
      "Result for 'pkg' directory:" + "\n" +
      get_files_info("calculator", "pkg") + "\n\n" +
      "Result for '/bin' directory:" + "\n" +
      get_files_info("calculator", "/bin") + "\n\n" +
      "Result for '../' directory:" + "\n" + 
      get_files_info("calculator", "../"))