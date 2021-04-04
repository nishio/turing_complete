"""
Two-color Cyclic Tag System
"""

import sys

def run(working, rules, limit=1):
    """
    >>> run('11011', ['101', '01', '0', '', '010'])
    '1101110101010101001001101010010010100010'
    """
    result = []
    rule_id = 0
    while len(working) >= limit:
        print(working)
        head = working[0]
        working = working[1:]
        result.append(head)
        if head == "1":
            working += rules[rule_id]
        rule_id = (rule_id + 1) % len(rules)
        if rule_id == 0:
            print(working)
            s = ""
            c2b = {'a': '100', 'b': '010', 'c': '001'}
            b2c = {c2b[k]:k for k in c2b}
            for i in range(0, len(working), 3):
                s += b2c[working[i:i+3]]
            print(s)
            print("-----")
            # input()
    print(working)

    return "".join(result)

def process_args(args):
    initial = args[0]
    rules = []
    for x in args[1:]:
        if x == '""':
            x = ""
        rules.append(x)
    print(run(initial, rules))

def _test():
    import doctest
    # doctest.testmod()
    run('100100100', ['010001', '100', '100100100', '', '', ''], limit=6)


def main():
    args = sys.argv[1:]
    process_args(args)

if __name__ == "__main__":
    if sys.argv[-1] == "-t":
        _test()
        sys.exit()
    main()