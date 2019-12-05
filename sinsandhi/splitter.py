from sinsandhi.rules.patterns import Patterns
from sinsandhi.rules.rules import Rules
from sinsandhi.utils.strings import process_string, convert_to_string

__all__ = [
    'split_word'
]


def split_word(w):

    cw = process_string(w)
    w_length = len(cw)
    splitted_words = []

    for rule in Rules:

        join = Patterns[rule['P']]['J']
        j_length = len(join[0])

        for i in range(0, w_length, 2):

            applicable = True

            lwb = cw[:i+join[1]]
            rwb = cw[i+join[2]:]

            lwl = []
            rwl = []

            lci = None if join[3] is None else i + join[3]
            lvi = None if join[4] is None else i + join[4]
            ici = None if join[5] is None else i + join[5]
            ivi = None if join[6] is None else i + join[6]
            rci = None if join[7] is None else i + join[7]
            rvi = None if join[8] is None else i + join[8]

            if ici is not None and (ici >= w_length or cw[ici] != rule['I']['C']):
                applicable = False
            if ivi is not None and (ivi >= w_length or cw[ivi] != rule['I']['V']):
                applicable = False

            if applicable:

                lp = Patterns[rule['P']]['L']
                if len(lp) > 0:
                    if lp == 'kCkV' and lci is not None and lvi is not None and cw[lci] in rule['L']['C'] and cw[lvi] in rule['L']['V']:
                        lwl.append(lwb + [cw[lci]] + [cw[lvi]])
                    elif lp == 'kCnV' and lci is not None and lvi is None and cw[lci] in rule['L']['C']:
                        lwl.append(lwb + [cw[lci]] + [None])
                    elif lp == 'kCdV' and lci is not None and lvi is None and cw[lci] in rule['L']['C']:
                        for v in rule['L']['V']:
                            lwl.append(lwb + [cw[lci]] + [v])
                    elif lp == 'dCdV' and lci is None and lvi is None:
                        for c in rule['L']['C']:
                            for v in rule['L']['V']:
                                lwl.append(lwb + [c] + [v])
                else:
                    lwl.append(lwb)

                rp = Patterns[rule['P']]['R']
                if len(rp) > 0:
                    if rp == 'nCkV' and rci is None and rvi is not None and \
                            rvi < w_length and cw[rvi] in rule['R']['V']:
                        rwl.append([None] + [cw[rvi]] + rwb)
                    elif rp == 'nCdV' and rci is None and rvi is None:
                        for v in rule['R']['V']:
                            rwl.append([None] + [v] + rwb)
                else:
                    lwl.append(lwb)

            for w1 in lwl:
                if w1 == cw:
                    continue
                for w2 in rwl:
                    splitted_words.append((convert_to_string(w1), convert_to_string(w2)))

    return splitted_words

