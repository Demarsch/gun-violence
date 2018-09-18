def split_value(value: str) -> dict:
    '''
    Converts string value that looks like 'key_0::value_0||key_1:value_1'
    into a dictionary { 'key_0': 'value_0', 'key_1': 'value1' }
    '''
    result = {}
    if not(value):
        return result
    items = value.split('||')
    for item in items:
        key_value = item.split('::')
        if len(key_value) > 1:
            result[key_value[0]] = result[key_value[1]]
    return result
