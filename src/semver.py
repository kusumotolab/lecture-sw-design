def isSemVer(v: str) -> bool:
    import re
    numeric = '(0|[1-9][0-9]*)'
    pattern = r'^%s.%s.%s$' % (numeric, numeric, numeric)
    return re.match(pattern, v) != None
