
from data_processing_files.variables import unique_bow, unique_element, unique_artifact, refinements_bows, bow_name, \
    element_type, artifact, refinement


def create_unique_names():
    create_unique_bow()
    create_unique_element()
    create_unique_artifact()


def create_unique_bow():
    for item in bow_name:
        if item not in unique_bow:
            unique_bow.append(item)
    for x in range(len(unique_bow)):
        print(unique_bow[x])


def create_unique_element():
    for item in element_type:
        if item not in unique_element:
            unique_element.append(item)
    for x in range(len(unique_element)):
        print(unique_element[x])


def create_unique_artifact():
    for item in artifact:
        if item not in unique_artifact:
            unique_artifact.append(item)
    for x in range(len(unique_artifact)):
        print(unique_artifact[x])
        print()


def fun():
    for x in range(len(unique_bow)):
        refinements_bows.append([])

    for x in range(len(bow_name)):
        index = (search_index(unique_bow, bow_name[x]))
        refinements_bows[index].append(refinement[x])

    # for i in range(len(refinements_bows)):
    # length = len(refinements_bows[i])
    # for j in range(length):
    # print(refinements_bows[i][j])


def search_index(arr, x):
    if x in arr:
        return arr.index(x)
