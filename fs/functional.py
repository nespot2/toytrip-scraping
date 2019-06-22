def curry(f):
    def result(a, *rest):
        if len(rest) > 0:
            return f(a, *rest)
        else:
            return lambda *r: f(a, *r)

    return result;


def reduce(f, acc, ite=[]):
    if len(ite) == 0:
        h, *t = acc
        acc = h
        ite = iter(t)

    for v in ite:
        acc = f(acc, v)

    return acc


c_map = curry(map)

c_filter = curry(filter)

c_reduce = curry(reduce)

