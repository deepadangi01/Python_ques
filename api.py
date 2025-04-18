import json
python_data={
    'name':'deepa',
    'age':25,
    'active':True
}
json_data=json.dumps(python_data)
print(json_data)
son_data='{"name": "deepa", "age": 25, "active": true}'
print(type(json_data))
python_data=json.loads(json_data)
print(python_data)
# check krne ke liye ki ye data json hai ya dict hai check datatype check
