from gendiff.scripts import gendiff
from gendiff.scripts import file_parsing


def test_parse_file_json():
    filepath = r"..\json_files\file1.json"
    result, status = file_parsing.parse_file(filepath)
    assert result == {"host": "hexlet.io", "timeout": 50, "proxy": "123.234.53.22", "follow": False}
    assert status == "OK"


def test_parse_file_yaml():
    filepath = r"..\json_files\file1.yaml"
    result, status = file_parsing.parse_file(filepath)
    assert result == {"host": "hexlet.io", "timeout": 50, "proxy": "123.234.53.22", "follow": False}
    assert status == "OK"


def test_generate_diff_json():
    json_file_1 = r"..\json_files\file1.json"
    json_file_2 = r"..\json_files\file2.json"
    diff = gendiff.generate_diff(json_file_1, json_file_2)
    assert diff == {
        '- follow': False,
        '  host': 'hexlet.io',
        '- proxy': '123.234.53.22',
        '- timeout': 50,
        '+ timeout': 20,
        '+ verbose': True
    }


def test_generate_diff_yaml():
    yaml_file_1 = r"..\json_files\file1.yaml"
    yaml_file_2 = r"..\json_files\file2.yaml"
    diff = gendiff.generate_diff(yaml_file_1, yaml_file_2)
    assert diff == {
        '- follow': False,
        '  host': 'hexlet.io',
        '- proxy': '123.234.53.22',
        '- timeout': 50,
        '+ timeout': 20,
        '+ verbose': True
    }


def test_formatter():
    data = {
        '- follow': False,
        '  host': 'hexlet.io',
        '- proxy': '123.234.53.22',
        '- timeout': 50,
        '+ timeout': 20,
        '+ verbose': True,
    }
    output = gendiff.formatter(data)
    assert output == '{\n  - follow: False\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + ' \
                     'timeout: 20\n  + verbose: True\n}'
