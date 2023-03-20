"""
Функция возвращает значение из словаря по переданному ключу, если ключ существует. В ином случае возвращается значение default.
"""


def get_val(collection, key, default='git'):
    if key not in collection:
        return default

    return collection[key]
