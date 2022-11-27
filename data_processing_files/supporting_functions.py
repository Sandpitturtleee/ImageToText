from data_processing_files.variables import bow_name_file_path, refinement_file_path, element_type_file_path, \
    element_value_file_path, artifact_file_path, bow_name, refinement, element_type, element_value, artifact


def read_values():
    read_bow_name()
    read_refinement()
    read_element_type()
    read_element_value()
    read_artifact()


def read_bow_name():
    temp = []
    with open(bow_name_file_path) as file:
        for line in file:
            if len(line) > 2:
                temp.append(line)
    for sub in temp:
        bow_name.append(sub.replace("\n", ""))


def read_refinement():
    temp = []
    with open(refinement_file_path) as file:
        for line in file:
            temp.append(line)
    for sub in temp:
        refinement.append(sub.replace("\n", ""))


def read_element_type():
    temp = []
    with open(element_type_file_path) as file:
        for line in file:
            if len(line) > 2:
                temp.append(line)
    for sub in temp:
        element_type.append(sub.replace("\n", ""))


def read_element_value():
    temp = []
    with open(element_value_file_path) as file:
        for line in file:
            temp.append(line)
    for sub in temp:
        element_value.append(sub.replace("\n", ""))


def read_artifact():
    with open(artifact_file_path) as file:
        for line in file:
            artifact.append(line)


def search_index(arr, x):
    if x in arr:
        return arr.index(x)


def write_data_to_file(folder_path, file_names, data):
    output_txt_filepaths = [None] * len(file_names)
    for x in range(len(output_txt_filepaths)):
        output_txt_filepaths[x] = folder_path + file_names[x] + ".txt"
        print(output_txt_filepaths[x])
        length = len(data[x])
        print(length)
        with open(output_txt_filepaths[x], 'w', encoding='utf-8') as f:
            for y in range(length):
                f.write("%s\n" % data[x][y])
