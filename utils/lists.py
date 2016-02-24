def id(xs):
    return xs

def head(xs : list) -> list:
    return xs[0]

def tail(xs : list) -> list:
    return xs[1:]

def init(xs : list) -> list:
    return xs[0:-1]

def last(xs : list) -> list:
    return xs[-1]

def singleton(item) -> list:
    return [item]

def addFirst(item, xs : list) -> list:
    return singleton(item) + xs

def addLast(item, xs : list) -> list:
    return list + singleton(item)

def isEmpty(xs : list) -> bool:
    return len(xs) == 0

def map(function, xs : list) -> list:
    return [function(item) for item in xs]

def reverse(xs : list) -> list:
    return xs[::-1]

def concat(xss : list) -> list:
    if (isEmpty(xss)):
        return []
    else:
        return head(xss) + concat(tail(xss))

def filter(predicate, xs: list) -> list:
    return [x for x in xs if predicate(x)]

def intersperse(item, xs : list) -> list:
    size = len(xs)
    if (size == 0 or size == 1):
        return xs
    else:
        return addFirst(head(xs),addFirst(item, intersperse(item, tail(xs))))

def intercalate(xs : list, xss : list) -> list:
    return concat((intersperse(xs,xss)))

def powerset(items : list) -> list:
    if (isEmpty(items)):
        return [[]]
    else:
        x = head(items)
        xs = tail(items)
        xss = powerset(xs)
        return xss + map(lambda ys: addFirst(x, ys), xss)

def foldLeft(function, initial, items : list):
    if (isEmpty(items)):
        return initial
    else:
        return function(foldLeft(function, initial, tail(items)), head(items))

def foldRight(function, initial, items : list):
    if (isEmpty(items)):
        return initial
    else:
        return function(last(items), foldRight(function, initial, init(items)))

def allMatch(predicate, items : list) -> bool:
    for item in items:
        if not predicate(item):
            return False
    return True

def anyMatch(predicate, items : list) -> bool:
    for item in items:
        if predicate(item):
            return True
    return False

def noneMatch(predicate, items : list) -> bool:
    return not anyMatch(predicate, items)

def zip(xs : list, ys : list) -> list:
    if isEmpty(xs):
        return []
    elif isEmpty(ys):
        return []
    else:
        return addFirst((head(xs), head(ys)), zip(tail(xs), tail(ys)))

def zipWith(combiner, xs : list, ys : list) -> list:
    if isEmpty(xs):
        return []
    elif isEmpty(ys):
        return []
    else:
        return addFirst(combiner(head(xs), head(ys)), zipWith(combiner, tail(xs), tail(ys)))

def partition(predicate, xs) -> (list, list):
    left = []
    right = []
    for x in xs:
        if (predicate(x)):
            right.append(x)
        else:
            left.append(x)
    return left, right

def quickSort(xs : list) -> list:
    if isEmpty(xs):
        return []
    else:
        pivot = head(xs)
        rest = tail(xs)
        smaller, greater = partition(lambda item: item > pivot, rest)
        return quickSort(smaller) + [pivot] + quickSort(greater)