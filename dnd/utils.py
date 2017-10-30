@staticmethod
def min_no_none(iterable):
    s = set(iterable)
    try:
        s.remove(None)
    except KeyError:
        pass
    if len(s) > 0:
        return min(s)
    return None
