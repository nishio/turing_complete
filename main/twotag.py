"""
 2-tag System
"""

def run(working, rules, delete=2):
    while len(working) >= delete:
        print(working)
        head = working[0]
        working = working[delete:] + rules[head]
    print(working)


def convert_to_cytag(working, rules):
    chars = list(rules)
    char_to_binary = {}
    N = len(chars)
    for i in range(N):
        buf = ["0"] * N
        buf[i] = "1"
        char_to_binary[chars[i]] = "".join(buf)

    new_rules = []
    for c in rules:
        binary_word = "".join(char_to_binary[x] for x in rules[c])
        new_rules.append(binary_word)
    for c in rules:
        new_rules.append("")  # mean: remove second character

    working = "".join(char_to_binary[x] for x in working)
    return working, new_rules, char_to_binary

TEST_T1 = """
Computation of Collatz sequences
https://en.wikipedia.org/wiki/Tag_system

>>> rules = {"a": "bc", "b": "a", "c": "aaa"}
>>> working = "aaa"
>>> run(working, rules)
aaa
abc
cbc
caaa
aaaaa
aaabc
abcbc
cbcbc
cbcaaa
caaaaaa
aaaaaaaa
aaaaaabc
aaaabcbc
aabcbcbc
bcbcbcbc
bcbcbca
bcbcaa
bcaaa
aaaa
aabc
bcbc
bca
aa
bc
a
"""

TEST_T2 = """
>>> rules = {"a": "bc", "b": "a", "c": "aaa"}
>>> working = "aaa"
>>> working, new_rules, char_to_binary = convert_to_cytag(working, rules)
>>> working
'100100100'
>>> new_rules
['010001', '100', '100100100', '', '', '']
>>> char_to_binary
{'a': '100', 'b': '010', 'c': '001'}
>>> import cytag
>>> cytag.run(working, new_rules, limit=6)
"""
def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            print(k)
            doctest.run_docstring_examples(g[k], g, name=k)

if __name__ == "__main__":
    import sys
    if sys.argv[-1] == "-t":
        _test()
        sys.exit()
    main()