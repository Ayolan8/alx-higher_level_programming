#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    r_value = list(a_dictionary.keys())[0]
    b_score = list(a_dictionary.values())[0]
    for x, y in a_dictionary.items():
        if y > b_score:
            b_score = y
            r_value = x
    return (r_value)
