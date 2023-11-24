def get_val(collection: dict, key, default='git'):
    for k, v in collection.items():
        if key in collection:
            return v
    if collection=={}:
        return default
