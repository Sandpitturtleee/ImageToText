from variables import bow_name


def bow_searching():
    unique_bow = []
    for item in bow_name:
        if item not in unique_bow:
            if len(item) > 2:
                unique_bow.append(item)

    for x in range(len(unique_bow)):
        print(unique_bow[x])
