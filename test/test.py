import json

text = {"a": 1, "b": 2, "c": 3}

json_text = json.dumps(text)

json_obj = json.loads(json_text)

print(type(json_obj))