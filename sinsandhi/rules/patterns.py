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

    Pattern Notation
    {
        '"Pattern Name/Key"': {
            'L': '"Suffix Pattern"',
            'R': '"Prefix Pattern"',
            'J': (
                '"Joined Sandhi Pattern"',
                "Left split idx",
                "Right split idx",
                "Left consonant idx or None",
                "Left vowel idx or None",
                "Inserted consonant idx or None"
                "Inserted vowel idx or None"
                "Right consonant idx or None",
                "Right vowel idx or None"
            )
        }
    }

"""

Patterns = {

    # Swara Sandhi Pattern
    'Pattern-O1': {
        'L': 'kCnV',
        'R': 'nCkV',
        'J': ('lCrV', 0, 2, 0, None, None, None, None, 1)
    },

    # Purwaswara Lopa Sandhi Pattern
    'Pattern-O2': {
        'L': 'kCdV',
        'R': 'nCkV',
        'J': ('lCrV', 0, 2, 0, None, None, None, None, 1)
    },

    # Paraswara Lopa Sandhi Pattern
    'Pattern-O3': {
        'L': 'kCkV',
        'R': 'nCdV',
        'J': ('lClV', 0, 2, 0, 1, None, None, None, None)
    },

    # Swaradesha Sandhi Pattern
    'Pattern-O4': {
        'L': 'kCdV',
        'R': 'nCdV',
        'J': ('lCiV', 0, 2, 0, None, None, 1, None, None)
    },

    # svara sandhi - guṇa sandhiya
    'Pattern-O5': {
        'L': 'kCdV',
        'R': 'nCdV',
        'J': ('lCiViCnV', 0, 4, 0, None, 2, 1, None, None)
    },

}
