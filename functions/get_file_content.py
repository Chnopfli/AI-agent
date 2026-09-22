import os

from openai.types.chat import ChatCompletionToolParam


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

schema_get_file_content: ChatCompletionToolParam = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads the content of a file (up to 10,000 characters)",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The relative path to the file that should be read.",
                },
            },
            "required": ["file_path"],
        },
    },
}