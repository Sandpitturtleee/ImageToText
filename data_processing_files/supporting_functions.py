from data_processing_files.variables import bow_name_file_path, refinement_file_path, element_type_file_path, \
    element_value_file_path, artifact_file_path, bow_name, refinement, element_type, element_value, artifact


def read_values():
    read_bow_name()
    read_refinement()
    read_element_type()
    read_element_value()
    read_artifact()


def read_bow_name():
    with open(bow_name_file_path) as file:
        for line in file:
            if len(line) > 2:
                bow_name.append(line)


def read_refinement():
    with open(refinement_file_path) as file:
        for line in file:
            refinement.append(line)


def read_element_type():
    with open(element_type_file_path) as file:
        for line in file:
            if len(line) > 2:
                element_type.append(line)


def read_element_value():
    with open(element_value_file_path) as file:
        for line in file:
            element_value.append(line)


def read_artifact():
    with open(artifact_file_path) as file:
        for line in file:
            artifact.append(line)


