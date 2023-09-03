
import concurrent.futures

def get_file_data(file_name):
    with open(file_name) as file:
        file_data = file.readlines()
    return file_data

def extract_functions(file_data):
    fun = []
    i = 0
    file_len = len(file_data)
    while i < file_len and " def " not in file_data[i]:
        i += 1
    one_fun = file_data[i]
    i += 1
    while i < file_len:
        if " def " in file_data[i]:
            fun.append(one_fun)
            one_fun = file_data[i]
        else:
            if "@" not in file_data[i]:
                one_fun += file_data[i]
        i += 1
    fun.append(one_fun.split("if __name__")[0])
    return fun

def get_functions_from_file(file_names: list):
    funs = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(get_file_data, file_names)
        for result in results:
            funs.extend(extract_functions(result))
    return funs
