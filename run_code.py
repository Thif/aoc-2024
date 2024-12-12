import sys
import importlib.util

CODE_FOLDER = "./code"


def load_module_from_path(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":

    day_str = str(sys.argv[1])
    input_folder_str = str(sys.argv[2])

    input_file_path = f"{input_folder_str}/{day_str}.txt"

    code_file_path = f"{CODE_FOLDER}/{day_str}.py"
    module_name = f"{CODE_FOLDER}.{day_str}"

    module = load_module_from_path(module_name, code_file_path)

    result = module.main(f"{input_folder_str}/{day_str}.txt")

    print(result)
