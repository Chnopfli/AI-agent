import os

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        path_to_target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, path_to_target_file]) == working_dir_abs
        
        if not os.path.isfile(path_to_target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        elif not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        else:
            MAX_CHARS: int = 10000
            with open(path_to_target_file, "r") as f:
                content: str = f.read(MAX_CHARS)
                if f.read(1):
                    content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                return content
   
    except Exception as e:
        return f"Error: {e}"