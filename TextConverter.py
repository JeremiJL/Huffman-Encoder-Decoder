def convert_to_string(file):
    content = ""
    with file.open("r") as f:
        for line in f:
            content += line
    return content


def convert_to_map(text):
    dist_map = dict()

    for letter in text:
        if letter not in dist_map.keys():
            dist_map[letter] = 1
        else:
            dist_map[letter] += 1

    return dist_map
