import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        path_to_target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, path_to_target_file]) == working_dir_abs
        
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        elif not os.path.isfile(path_to_target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        elif not path_to_target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        else:
            command = ["python", path_to_target_file]

            if args:
                command.extend(args)

            com_value = subprocess.run(command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30)

            output_parts = []

            if com_value.returncode != 0:
                output_parts.append(f"Process exited with code {com_value.returncode}")

            if not com_value.stdout and not com_value.stderr:
                output_parts.append("No output produced")

            else:
                if com_value.stdout:
                    output_parts.append(f"STDOUT: {com_value.stdout}")
                if com_value.stderr:
                    output_parts.append(f"STDERR: {com_value.stderr}")
            return "\n".join(output_parts)

    except Exception as e:
        return f"Error: executing Python file: {e}"
