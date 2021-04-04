"""
2-Tag System and Turing Machine
Cocke, J., and Minsky, M.: "Universality of Tag Systems with P=2", J. Assoc. Comput. Mach. 11, 15–20, 1964.
[PDF https://dspace.mit.edu/bitstream/handle/1721.1/6107/AIM-052.pdf?sequence=2]



State: string starts with "Q"

Tag System
Character: string

"""


turing_rules = {  # state: (write, move, if 0 goto, if 1 goto)
    "Qstart": (0, "R", "Q1_1", "Q1_0")
}

def turing_step(rules, state, left_tape, right_tape):
    write, move, if0, if1 = rules[state]
    if move == "R":
        left_tape.append(write)
        if right_tape:
            read = right_tape[0]
            right_tape = right_tape[1:]
        else:
            read = 0
            right_tape = []

    else:
        right_tape.insert(0, write)
        if left_tape:
            read = left_tape[-1]
            left_tape = left_tape[:-1]
        else:
            read = 0
            left_tape = []
    if read:
        new_state = if1
    else:
        new_state = if0
    return new_state, left_tape, right_tape


def convert(turing_rules):
    tag_rules = {}
    for state in turing_rules:
        write, move, if0, if1 = turing_rules[state]
        if move == "L":
            raise NotImplemented

        def add_rule(key, value, new_state=state):
            tag_rules[f"{key}_{state}"] = [f"{v}_{new_state}" for v in value.split()]

        if write:
            add_rule("A", "C x c x")
        else:
            add_rule("A", "C x")

        add_rule("a", "c x")
        add_rule("B", "S")
        add_rule("b", "s")
        add_rule("C", "D1 D0")
        add_rule("c", "d1 d0")
        add_rule("S", "T1 T0")
        add_rule("s", "t1 t0")
        add_rule("D1", "A x", new_state=if1)
        add_rule("d1", "a x", new_state=if1)
        add_rule("T1", "B x", new_state=if1)
        add_rule("t1", "b x", new_state=if1)
        add_rule("D0", "x A x", new_state=if0)
        add_rule("d0", "a x", new_state=if0)
        add_rule("T0", "B x", new_state=if0)
        add_rule("t0", "b", new_state=if0)
    return tag_rules

def run_tag_system(turing_rules, initial_state, left_tape, right_tape):
    tag_rules = convert(turing_rules)
    queue = get_initial_queue(initial_state, left_tape, right_tape)
    while len(queue) >= 2:
        print(queue)
        head = queue[0]
        if head not in tag_rules:
            break
        queue = queue[2:] + tag_rules[head]
    print(queue)
    return queue


def get_initial_queue(initial_state, left_tape, right_tape):
    M = 0
    for x in left_tape:
        M *= 2
        M += x
    N = 0
    for x in reversed(right_tape):
        N *= 2
        N += x
    
    ax = "ax"
    bx = "bx"
    initial_queue = [
        f"{c}_{initial_state}"
        for c in f"Ax{ax * M}Bx{bx * N}"
    ]
    return initial_queue
