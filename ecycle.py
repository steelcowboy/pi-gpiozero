def cycle(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    saved = []
    for element in iterable:
        saved.append(element)
    while saved:
        for element in saved:
            yield element
        for element in reversed(saved):
            yield element
