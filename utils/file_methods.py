import json


def write_array(path, arr):
    with open(path, 'w+') as f:
        for elem in arr:
            f.write(elem + '\n')


def read_json(path):
    data = []
    with open(path) as f:
        for line in f:
            data.append(json.loads(line))
    return data


def read_file_line(path):
    res = []
    with open(path) as f:
        for line in f:
            res.append(line.replace('\n', ''))
    return res


def write_string(path, str_):
    with open(path, 'w+') as f:
        f.write(str_)