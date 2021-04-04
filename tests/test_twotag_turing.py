import pytest
import main
from main.twotag_turing import convert, turing_step, run_tag_system, get_initial_queue

def test_rules():
    rules = {  # state: (write, move, if 0 goto, if 1 goto)
       "Qstart": (0, "R", "Q1_1", "Q1_0")
    }
    r = convert(rules)
    print(r)
    assert len(r) == 16
    assert r == {'A_Qstart': ['C_Qstart', 'x_Qstart'], 'a_Qstart': ['c_Qstart', 'x_Qstart'], 'B_Qstart': ['S_Qstart'], 'b_Qstart': ['s_Qstart'], 'C_Qstart': ['D1_Qstart', 'D0_Qstart'], 'c_Qstart': ['d1_Qstart', 'd0_Qstart'], 'S_Qstart': ['T1_Qstart', 'T0_Qstart'], 's_Qstart': ['t1_Qstart', 't0_Qstart'], 'D1_Qstart': ['A_Q1_0', 'x_Q1_0'], 'd1_Qstart': ['a_Q1_0', 'x_Q1_0'], 'T1_Qstart': ['B_Q1_0', 'x_Q1_0'], 't1_Qstart': ['b_Q1_0', 'x_Q1_0'], 'D0_Qstart': ['x_Q1_1', 'A_Q1_1', 'x_Q1_1'], 'd0_Qstart': ['a_Q1_1', 'x_Q1_1'], 'T0_Qstart': ['B_Q1_1', 'x_Q1_1'], 't0_Qstart': ['b_Q1_1']}

def test_turing_step():
    rules = {  # state: (write, move, if 0 goto, if 1 goto)
       "Qstart": (0, "R", "Q1_0", "Q1_1")
    }
    assert turing_step(rules, "Qstart", [], []) == ('Q1_0', [0], [])
    assert turing_step(rules, "Qstart", [], [1]) == ('Q1_1', [0], [])

def test_get_initial_queue():
    rules = {  # state: (write, move, if 0 goto, if 1 goto)
       "Qstart": (0, "R", "Q1_0", "Q1_1")
    }
    assert get_initial_queue("Qstart", [], []) == ['A_Qstart', 'x_Qstart', 'B_Qstart', 'x_Qstart']
    assert get_initial_queue("Qstart", [], [1]) == ['A_Qstart', 'x_Qstart', 'B_Qstart', 'x_Qstart', 'b_Qstart', 'x_Qstart']

def test_run_tag_system():
    rules = {  # state: (write, move, if 0 goto, if 1 goto)
       "Qstart": (0, "R", "Q1_0", "Q1_1")
    }
    assert run_tag_system(rules, "Qstart", [], [])[0] == 'A_Q1_0'
    assert run_tag_system(rules, "Qstart", [], [1])[0] == 'A_Q1_1'