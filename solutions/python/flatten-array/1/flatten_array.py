def flatten(iterable):
    result = []
    for itr in iterable:
        if isinstance(itr,list):
            result.extend(flatten(itr))
        else:
            if itr != " " and itr is not None:
                result.append(itr)

    return result
