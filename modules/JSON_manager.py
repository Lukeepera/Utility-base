import json

def json_minify(input_string):
    try:
        return json.dumps(json.loads(input_string), separators=(',', ':'))
    except json.JSONDecodeError as e:
        return f"Invalid JSON: {e}"

def json_beautify(input_string):
    try:
        return json.dumps(json.loads(input_string), indent=2)
    except json.JSONDecodeError as e:
        return f"Invalid JSON: {e}"

def minify_file(json_content):
    try:
        return json.dumps(json.loads(json_content), separators=(',', ':'))
    except json.JSONDecodeError as e:
        return f"Invalid JSON: {e}"

def beautify_file(json_content):
    try:
        return json.dumps(json.loads(json_content), indent=2)
    except json.JSONDecodeError as e:
        return f"Invalid JSON: {e}"
