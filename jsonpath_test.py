
import jsonpath

resp_json = {
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
            },
            {
                "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
            },
            {
                "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99
            },
            {
                "category": "fiction",
                "author": "J. R. R. Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
            }
        ],
        "bicycle": {
            "color": "red",
            "price": "195"
        }
    },
    "expensive": 10
}
resp_json = {
    'success': "True",
    'error_code': "0",
    'error_msg': '成功',
    'result': {
        'confirmToShipTime': {'current': 7.68, 'compareTo30Days': 10.34},
        'confirmToScanTime': {'current': 10.56, 'compareTo30Days': 15.78},
        'confirmToSignTime': {'current': 81.12, 'compareTo30Days': 23.8},
        'shipToSignTime': {'current': 74.16, 'compareTo30Days': 26.63},
        'shipToScanTime': {'current': 2.88, 'compareTo30Days': 33.33},
        'scanToSignTime': {'current': 71.28, 'compareTo30Days': 26.92},
        'expressComplaintRate': {'current': 0.0014, 'compareTo30Days': 180.0},
        'expressIntegrityRate': {'current': 0.409, 'compareTo30Days': 4.15},
        'shipTotalCount': {'current': 50038, 'compareTo30Days': -0.11},
        'shipProvinceId': 6, 'shipProvinceName': '广东省', 'stateDate': '2021-02-24'}}

bicycle = {
        "color": {"current": "red", "value": "123", "key": "one"},
        "price": {"current": "195"}
    }
# rule = '$.store.book'
# field = {
#     "category": ""
# }

rule = '$.result'
value = jsonpath.jsonpath(resp_json, rule)[0]
# print(value)
# rule = '$.store.bicycle'
field = {
    "confirmToScanTime": "",
    "confirmToShipTime": "",
    "confirmToSignTime": "",
    "expressComplaintRate": "",
    "expressIntegrityRate": "",
    "scanToSignTime": "",
    "shipToSignTime": "",
    "shipTotalCount": ""
}
dict_key = "current"
item = {}
# value = jsonpath.jsonpath(resp_json, rule)[0]
#
if isinstance(value, list):
    for value_one in value:
        for key, key_value in field.items():
            item[key] = value_one[key]
        print(item)

elif isinstance(value, dict):
    for key, key_value in field.items():
        if not isinstance(value[key], dict):
            item[key] = value[key]
        else:
            # for key_next, value_next in value[key].items():
            item[key] = value[key][dict_key]
    print(item)
# value = jsonpath.jsonpath(resp_json, '$..price')
# value = jsonpath.jsonpath(resp_json, '$.store.book')[0]
# for value_one in value:
#     category = value_one['category']
#     print(category)