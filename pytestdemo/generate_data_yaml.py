import yaml

data = {
    'add': {
        'data': [[1, 2, 3], [1, 3, 4], [2, 3, 5], ['哇擦', '啊哈', False]],
        'ids': ['[1, 2]', '[1, 3]', '[2, 3]', '[\'哇擦\', \'啊哈\']']
    },
    'divide': {
        'data': [[0, 1, 0], [1, 0, False], [1, 1, 1], ['吆西', '八嘎', False]],
        'ids': ['[0, 1]', '[1, 0]', '[1, 1]', '[\'吆西\', \'八嘎\']']
    }
}
with open('./data/data.yaml', 'w') as f:
    yaml.safe_dump(data, f)
