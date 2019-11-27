from sinsandhi.rules.patterns import Patterns
from sinsandhi.rules.rules import Rules
from sinsandhi.utils.strings import process_string, convert_to_string

__all__ = [
    'join_words'
]


def suffix_match(word, v):
    if word[-2] in v['C'] and word[-1] in v['V']:
        return True
    else:
        return False


def prefix_match(word, v):
    if word[0] in v['C'] and word[1] in v['V']:
        return True
    else:
        return False


def calculate_lji(word):
    lji = len(word)
    # if len(pattern_str) > 0:
    #     if pattern_str[0] == 'd':
    #         return lji - 2
    #     elif pattern_str[2] == 'n' or pattern_str[2] == 'd':
    #         return lji - 1
    return lji - 2


def calculate_rji(word):
    # if len(pattern_str) > 0:
    #     if pattern_str[0] == 'n' or pattern_str[0] == 'd':
    #         if pattern_str[2] == 'k':
    #             return 2
    return 2


def join_words(l, r):

    lw = process_string(l)
    rw = process_string(r)
    joined_words = []

    for rule in Rules:
        l_match = suffix_match(lw, rule['L'])
        r_match = prefix_match(rw, rule['R'])

        if l_match and r_match:

            lji = calculate_lji(lw)
            rji = calculate_rji(rw)

            middle = []
            join_str = Patterns[rule['P']]['J']
            for i in range(0, len(join_str), 2):
                if join_str[i:i+2] == 'lC':
                    middle.append(lw[-2])
                if join_str[i:i+2] == 'lV':
                    middle.append(lw[-1])
                elif join_str[i:i+2] == 'rV':
                    middle.append(rw[1])

            joined_word = lw[:lji] + middle + rw[rji:]
            joined_words.append(convert_to_string(joined_word))

    return joined_words


class Joiner:
    pass




