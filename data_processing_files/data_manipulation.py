from data_processing_files.supporting_functions import search_index
from data_processing_files.variables import unique_bow, unique_element, unique_artifact, refinements_bows, bow_name, \
    element_type, artifact, refinement, values_elements, element_value, unique_artifact_count


# for i in range(len(refinements_bows)):
# length = len(refinements_bows[i])
# for j in range(length):
# print(refinements_bows[i][j])

def create_unique_names():
    create_unique_bow()
    create_unique_element()
    create_unique_artifact()


def create_unique_bow():
    for item in bow_name:
        if item not in unique_bow:
            unique_bow.append(item)


def create_unique_element():
    for item in element_type:
        if item not in unique_element:
            unique_element.append(item)


def create_unique_artifact():
    for item in artifact:
        if item not in unique_artifact:
            unique_artifact.append(item)
    for x in range(len(unique_artifact)):
        print(unique_artifact[x])
        print()


def group_refinements():
    for x in range(len(unique_bow)):
        refinements_bows.append([])
    for x in range(len(bow_name)):
        index = (search_index(unique_bow, bow_name[x]))
        refinements_bows[index].append(refinement[x])


def group_dmg_bonuses():
    for x in range(len(unique_element)):
        values_elements.append([])
    for x in range(len(element_type)):
        index = (search_index(unique_element, element_type[x]))
        values_elements[index].append(element_value[x])


def count_artifacts():
    for x in range(len(unique_artifact)):
        unique_artifact_count.append(0)
    for x in range(len(artifact)):
        index = (search_index(unique_artifact, artifact[x]))
        unique_artifact_count[index] += 1

