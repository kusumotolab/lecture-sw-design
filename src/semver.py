
def isSemVer(ver):
    import re
    numeric = '(0|[1-9][0-9]*)'
    pattern = r'^%s.%s.%s$' % (numeric, numeric, numeric)
    return re.match(pattern, ver) != None
