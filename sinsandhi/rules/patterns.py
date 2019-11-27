"""
    This file define the patters that can be observed in Sandhi Rules

    Notations
        C - Consonant
        V - Vowel

        k - Keep
        d - Delete
        n - No
        i - Insert
        l - Left
        r - Right

"""

Patterns = {

    # Swara Sandhi Pattern
    'Pattern-O1': {
        'L': 'kCnV',
        'R': 'nCkV',
        'J': 'lCrV'
    },

    # Purwaswara Lopa Sandhi Pattern
    'Pattern-O2': {
        'L': 'kCdV',
        'R': 'nCkV',
        'J': 'lCrV'
    },

    # Paraswara Lopa Sandhi Pattern
    'Pattern-O3': {
        'L': 'kCkV',
        'R': 'nCdV',
        'J': 'lClV'
    },


}
