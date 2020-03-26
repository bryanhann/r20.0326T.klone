def extract(prefix, _dict):
    acc = dict()
    for k,v in _dict.items():
        if k.startswith(prefix):
            acc[ k[len(prefix):] ] = v
    return acc

