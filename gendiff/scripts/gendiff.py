import argparse
from typing import Union
from .file_parsing import parse_file


def gendiff():
    args = parser.parse_args()
    difference: dict = generate_diff(args.filename_1, args.filename_2)
    result = formatter(difference)
    print(result)


def generate_diff(filepath_1: str, filepath_2: str) -> Union[dict, str]:
    def walk(subdict1, subdict2, res: dict):
        all_keys = list(subdict1.keys()) + list(subdict2.keys())
        for i in range(len(all_keys) - 1, -1, -1):
            if all_keys.count(all_keys[i]) > 1:
                del all_keys[i]
        for k in all_keys:
            try:
                value1 = subdict1[k]
                try:
                    value2 = subdict2[k]

                    if value1 == value2:
                        both_key = f"{status_code['both']} {k}"
                        res[both_key] = value1
                    else:
                        if type(value1) == dict and type(value2) == dict:
                            both_key = f"{status_code['both']} {k}"
                            res[both_key] = walk(value1, value2, {})
                        else:
                            key_1 = f"{status_code['only_1']} {k}"
                            key_2 = f"{status_code['only_2']} {k}"
                            res[key_1] = value1
                            res[key_2] = value2

                except KeyError:
                    key_1 = f"{status_code['only_1']} {k}"
                    if type(value1) != dict:
                        res[key_1] = value1
                    else:
                        res[key_1] = sort_dict(value1)

            except KeyError:
                key_2 = f"{status_code['only_2']} {k}"
                if type(subdict2[k]) != dict:
                    res[key_2] = subdict2[k]
                else:
                    res[key_2] = sort_dict(subdict2[k])

        return res

    # проверяем file1 и file2 на существуемость и на возможность открыть:
    file1, status1 = parse_file(filepath_1)
    file2, status2 = parse_file(filepath_2)

    if status1 and status2:
        difference = {}
        status_code = {"both": " ", "only_1": "-", "only_2": "+"}
        return walk(file1, file2, difference)
    else:
        return "An error occurred"


def sort_dict(some_dict: dict):
    fk: str = list(some_dict.keys())[0]
    if fk.startswith('  ') or fk.startswith('+') or fk.startswith('-'):
        return dict(sorted(list(some_dict.items()), key=lambda x: x[0][2:]))
    else:
        return dict(sorted(list(some_dict.items()), key=lambda x: x[0]))


def formatter(tree: Union[dict, str]) -> str:
    def walk(subtree: dict, sub_step: str) -> str:
        subtree = sort_dict(subtree)
        sub_str = ''
        for k, v in subtree.items():
            if type(v) == dict:
                next_step = sub_step + "    "
                sub_str += sub_step + k + ": {\n" + walk(v, next_step)
                if "+" in k or "-" in k:
                    sub_str += sub_step + "  }\n"
                else:
                    sub_str += sub_step + "}\n"
            else:
                sub_str += f"{sub_step}{k}: {v}\n"

        return sub_str

    if type(tree) == dict:
        step = "  "
        return '{\n' + walk(tree, step) + "}"
    else:
        return tree


parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('filename_1', metavar='first_file', type=str, help='Filename to compare')
parser.add_argument('filename_2', metavar='second_file', type=str, help='Filename to compare')
parser.add_argument('-f', '--format', metavar='FORMAT',
                    help='set format of output')

if __name__ == '__main__':
    gendiff()
