id = lambda x: x
negate = lambda x: not x

plus = lambda x, y: x + y
minus = lambda x, y: x - y
mult = lambda x, y: x * y
div = lambda x, y: x / y
intdiv = lambda x, y: x // y
pow = lambda x, y: x ** y

eq = lambda x, y: x == y
neq = lambda x, y: x != y
gt = lambda x, y: x > y
st = lambda x, y: x < y
gteq = lambda x, y: x >= y
steq = lambda x, y: x <= y

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
    return xs + singleton(item)

def isEmpty(xs : list) -> bool:
    return len(xs) == 0

def map(function, xs : list) -> list:
    return [function(item) for item in xs]

def reverse(xs : list) -> list:
    return xs[::-1]

def concat(xs : list, ys : list) -> list:
    return xs + ys

def concatMany(zss : list) -> list:
    return foldLeft(concat, [], zss)

def forEach(consumer, iterable):
    for item in iterable:
        consumer(item)
    return iterable

def filter(predicate, xs: list) -> list:
    return [x for x in xs if predicate(x)]

def intersperse(item, xs : list) -> list:
    size = len(xs)
    if (size == 0 or size == 1):
        return xs
    else:
        return addFirst(head(xs),addFirst(item, intersperse(item, tail(xs))))

def intercalate(xs : list, xss : list) -> list:
    return concatMany(intersperse(xs,xss))

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

def flatMap(generator, xs : list) -> list:
    return foldLeft(concatMany, [], map(generator, xs))

def sum(xs : list):
    return foldLeft(plus, 0, xs)

def product(xs : list):
    return foldLeft(mult, 1, xs)

def minimum(xs : list):
    if (len(xs) == 1):
        return head(xs)
    else:
        return min(head(xs), minimum(tail(xs)))

def maximum(xs : list):
    if (len(xs) == 1):
        return head(xs)
    else:
        return max(head(xs), maximum(tail(xs)))

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

def unzip(zs : list) -> (list, list):
    (left, right) = ([], [])
    for (x, y) in zs:
        left.append(x)
        right.append(y)
    return (left, right)

def zipWith(combiner, xs : list, ys : list) -> list:
    if isEmpty(xs):
        return []
    elif isEmpty(ys):
        return []
    else:
        return addFirst(combiner(head(xs), head(ys)), zipWith(combiner, tail(xs), tail(ys)))

def take(n, xs : list) -> list:
    return xs[:n]

def drop(n, xs : list) -> list:
    return xs[n:]

def takeWhile(predicate, xs : list) -> list:
    if isEmpty(xs):
        return []
    i = 0
    while (i < len(xs)):
        x = xs[i]
        if predicate(x):
            i += 1
        else:
            break
    return take(i, xs)

def dropWhile(predicate, xs : list) -> list:
    if isEmpty(xs):
        return []
    i = 0
    while (i < len(xs)):
        x = xs[i]
        if predicate(x):
            i += 1
        else:
            break
    return drop(i, xs)

def splitAt(n : int, xs : list) -> (list, list):
    (left, right) = ([],[])
    i = 0
    while (i < n and i < len(xs)):
        left.append(xs[i])
        i += 1
    while (i < len(xs)):
        right.append(xs[i])
        i += 1
    return (left, right)

def partition(predicate, xs) -> (list, list):
    left = []
    right = []
    for x in xs:
        if (predicate(x)):
            right.append(x)
        else:
            left.append(x)
    return left, right

def merge(xs : list, ys : list) -> list:
    if (isEmpty(xs)):
        return ys
    if (isEmpty(ys)):
        return xs
    x = head(xs)
    y = head(ys)
    if (x > y):
        return addFirst(y, merge(xs, tail(ys)))
    else:
        return addFirst(x, merge(tail(xs), ys))

def mergeSort(zs : list) -> list:
    if (len(zs) < 2):
        return zs
    else:
        (xs, ys) = splitAt(len(zs) // 2, zs)
        return merge(mergeSort(xs), mergeSort(ys))

def quickSort(xs : list) -> list:
    if isEmpty(xs):
        return []
    else:
        pivot = head(xs)
        rest = tail(xs)
        smaller, greater = partition(lambda item: item > pivot, rest)
        return quickSort(smaller) + [pivot] + quickSort(greater)

def mergeBy(xs : list, ys : list, comparator) -> list:
    if (isEmpty(xs)):
        return ys
    if (isEmpty(ys)):
        return xs
    x = head(xs)
    y = head(ys)
    if (comparator(x, y) > 0):
        return addFirst(y, mergeBy(xs, tail(ys), comparator))
    else:
        return addFirst(x, mergeBy(tail(xs), ys, comparator))

def mergeSortBy(zs : list, comparator) -> list:
    if (len(zs) < 2):
        return zs
    else:
        (xs, ys) = splitAt(len(zs) // 2, zs)
        return mergeBy(mergeSortBy(xs, comparator), mergeSortBy(ys, comparator), comparator)

def quickSortBy(xs : list, comparator) -> list:
    if isEmpty(xs):
        return []
    else:
        pivot = head(xs)
        rest = tail(xs)
        smaller, greater = partition(lambda item: comparator(item, pivot) > 0, rest)
        return quickSortBy(smaller, comparator) + [pivot] + quickSortBy(greater, comparator)

def minBy(comparator, x, y):
    if (comparator(x, y) < 0):
        return x
    else:
        return y

def maxBy(comparator, x, y):
    if (comparator(x, y) > 0):
        return x
    else:
        return y

def minimumBy(xs, comparator):
    return foldLeft(lambda x, y : minBy(comparator, x, y), head(xs), tail(xs))

def maximumBy(xs, comparator):
    return foldLeft(lambda x, y : maxBy(comparator, x, y), head(xs), tail(xs))