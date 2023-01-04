from data_processing_files.variables import bow_name_file_path, refinement_file_path, element_type_file_path, \
    element_value_file_path, artifact_file_path, bow_name, refinement, element_type, element_value, artifact, \
    unique_artifact_count, unique_artifact, unique_bow, unique_bow_count, folder_path_data_bows, refinements_bows, \
    folder_path_data_elements, unique_element, values_elements, folder_path_data_artifacts


def read_values():
    read_bow_name()
    read_refinement()
    read_element_type()
    read_element_value()
    read_artifact()


def write_to_files():
    write_data_to_file(folder_path_data_bows, unique_bow, refinements_bows)
    write_data_to_file(folder_path_data_elements, unique_element, values_elements)
    write_artifact_to_file(folder_path_data_artifacts, unique_artifact_count)
    write_bow_to_file(folder_path_data_bows, unique_bow_count)


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
    temp = []
    with open(artifact_file_path) as file:
        for line in file:
            if len(line) > 2:
                temp.append(line)
    for sub in temp:
        artifact.append(sub.replace("\n", ""))


def search_index(arr, x):
    if x in arr:
        return arr.index(x)


def write_data_to_file(folder_path, file_names, data):
    output_txt_filepaths = [None] * len(file_names)
    for x in range(len(output_txt_filepaths)):
        output_txt_filepaths[x] = folder_path + file_names[x] + ".txt"
        length = len(data[x])
        with open(output_txt_filepaths[x], 'w', encoding='utf-8') as f:
            for y in range(length):
                f.write("%s\n" % data[x][y])


def write_artifact_to_file(folder_path, data):
    output_txt_filepath_names = folder_path + "Artifacts_names" + ".txt"
    output_txt_filepath_values = folder_path + "Artifacts_values" + ".txt"
    with open(output_txt_filepath_names, 'w', encoding='utf-8') as f:
        for x in range(len(unique_artifact)):
            f.write("%s\n" % unique_artifact[x])
    with open(output_txt_filepath_values, 'w', encoding='utf-8') as f:
        for x in range(len(unique_artifact_count)):
            f.write("%s\n" % data[x])


def write_bow_to_file(folder_path, data):
    output_txt_filepath_names = folder_path + "Bow_names" + ".txt"
    output_txt_filepath_values = folder_path + "Bow_values" + ".txt"
    with open(output_txt_filepath_names, 'w', encoding='utf-8') as f:
        for x in range(len(unique_bow)):
            f.write("%s\n" % unique_bow[x])
    with open(output_txt_filepath_values, 'w', encoding='utf-8') as f:
        for x in range(len(unique_bow_count)):
            f.write("%s\n" % data[x])
