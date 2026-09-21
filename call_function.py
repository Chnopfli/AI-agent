from functions.get_files_info import schema_get_files_info
from openai.types.chat import ChatCompletionToolParam

available_functions: list[ChatCompletionToolParam] = [
    schema_get_files_info,
]