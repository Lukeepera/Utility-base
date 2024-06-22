import pytest
from modules.JSON_manager import json_minify, json_beautify, minify_file, beautify_file

def test_json_minify():
    input_string = '{"name": "John", "age": 30}'
    expected_output = '{"name":"John","age":30}'
    assert json_minify(input_string) == expected_output

def test_json_minify_invalid():
    input_string = '{"name": "John", "age": 30'
    assert "Invalid JSON" in json_minify(input_string)

def test_json_beautify():
    input_string = '{"name": "John", "age": 30}'
    expected_output = '{\n  "name": "John",\n  "age": 30\n}'
    assert json_beautify(input_string) == expected_output

def test_json_beautify_invalid():
    input_string = '{"name": "John", "age": 30'
    assert "Invalid JSON" in json_beautify(input_string)

def test_minify_file():
    json_content = '{"name": "John", "age": 30}'
    expected_output = '{"name":"John","age":30}'
    assert minify_file(json_content) == expected_output

def test_minify_file_invalid():
    json_content = '{"name": "John", "age": 30'
    assert "Invalid JSON" in minify_file(json_content)

def test_beautify_file():
    json_content = '{"name": "John", "age": 30}'
    expected_output = '{\n  "name": "John",\n  "age": 30\n}'
    assert beautify_file(json_content) == expected_output

def test_beautify_file_invalid():
    json_content = '{"name": "John", "age": 30'
    assert "Invalid JSON" in beautify_file(json_content)
