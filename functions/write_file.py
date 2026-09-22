import os

from openai.types.chat import ChatCompletionToolParam

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        path_to_target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, path_to_target_file]) == working_dir_abs
        
        if os.path.isdir(path_to_target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        elif not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        else:
            os.makedirs(os.path.dirname(path_to_target_file), exist_ok=True)
            with open(path_to_target_file, "w") as f:
                f.write(content)
                return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"

schema_write_file: ChatCompletionToolParam = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes content to a file. Overwrites existing files and creates directories if needed.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The relative path to the file where the content should be written.",
                },
                "content": {
                    "type": "string",
                    "description": "The full text content to write into the file.",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}
