from functions.get_files_info import get_files_info

print("Result for current directory:" + "\n" +
      get_files_info("calculator", ".") + "\n" +
      "Result for 'pkg' directory:" + "\n" +
      get_files_info("calculator", "pkg") + "\n" +
      "Result for '/bin' directory:" + "\n" +
      get_files_info("calculator", "/bin") + "\n" +
      "Result for '../' directory:" + "\n" + 
      get_files_info("calculator", "../"))