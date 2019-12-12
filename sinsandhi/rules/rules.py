"""
    This file define the Sandhi Rules based on the patterns
"""

Rules = [

    # Swara Sandhi
    {
        'P': 'Pattern-O1',
        'L': {
            'C': [
                'ක්', 'ඛ්', 'ග්', 'ඝ්', 'ඞ්', 'ඟ්', 'ච්', 'ඡ්', 'ජ්', 'ඣ්', 'ඤ්', 'ඦ්',
                'ට්', 'ඨ්', 'ඩ්', 'ඪ්', 'ණ්', 'ඬ්', 'ත්', 'ථ්', 'ද්', 'ධ්', 'න්', 'ඳ්',
                'ප්', 'ඵ්', 'බ්', 'භ්', 'ම්', 'ඹ්', 'ය්', 'ර්', 'ල්', 'ව්',
                'ශ්', 'ෂ්', 'ස්', 'හ්', 'ළ්', 'ෆ්'
            ],
            'V': [None]
        },
        'R': {
            'C': [None],
            'V': [
                'අ', 'ආ', 'ඇ', 'ඈ', 'ඉ', 'ඊ', 'උ', 'ඌ', 'ඍ', 'ඎ', 'එ', 'ඒ', 'ඓ', 'ඔ', 'ඕ', 'ඖ',
            ]
        }
    },

    # Purwaswara Lopa Sandhi
    {
        'P': 'Pattern-O2',
        'L': {
            'C': [
                'ක්', 'ඛ්', 'ග්', 'ඝ්', 'ඞ්', 'ඟ්', 'ච්', 'ඡ්', 'ජ්', 'ඣ්', 'ඤ්', 'ඦ්',
                'ට්', 'ඨ්', 'ඩ්', 'ඪ්', 'ණ්', 'ඬ්', 'ත්', 'ථ්', 'ද්', 'ධ්', 'න්', 'ඳ්',
                'ප්', 'ඵ්', 'බ්', 'භ්', 'ම්', 'ඹ්', 'ය්', 'ර්', 'ල්', 'ව්',
                'ශ්', 'ෂ්', 'ස්', 'හ්', 'ළ්', 'ෆ්'
            ],
            'V': [
                'අ', 'ආ', 'ඇ', 'ඈ', 'ඉ', 'ඊ', 'උ', 'ඌ', 'ඍ', 'ඎ', 'එ', 'ඒ', 'ඓ', 'ඔ', 'ඕ', 'ඖ',
            ]
        },
        'R': {
            'C': [None],
            'V': [
                'අ', 'ආ', 'ඇ', 'ඈ', 'ඉ', 'ඊ', 'උ', 'ඌ', 'ඍ', 'ඎ', 'එ', 'ඒ', 'ඓ', 'ඔ', 'ඕ', 'ඖ',
            ]
        }
    },

    # Paraswara Lopa Sandhi
    {
        'P': 'Pattern-O3',
        'L': {
            'C': [
                'ක්', 'ඛ්', 'ග්', 'ඝ්', 'ඞ්', 'ඟ්', 'ච්', 'ඡ්', 'ජ්', 'ඣ්', 'ඤ්', 'ඦ්',
                'ට්', 'ඨ්', 'ඩ්', 'ඪ්', 'ණ්', 'ඬ්', 'ත්', 'ථ්', 'ද්', 'ධ්', 'න්', 'ඳ්',
                'ප්', 'ඵ්', 'බ්', 'භ්', 'ම්', 'ඹ්', 'ය්', 'ර්', 'ල්', 'ව්',
                'ශ්', 'ෂ්', 'ස්', 'හ්', 'ළ්', 'ෆ්'
            ],
            'V': [
                'අ', 'ආ', 'ඇ', 'ඈ', 'ඉ', 'ඊ', 'උ', 'ඌ', 'ඍ', 'ඎ', 'එ', 'ඒ', 'ඓ', 'ඔ', 'ඕ', 'ඖ',
            ]
        },
        'R': {
            'C': [None],
            'V': [
                'අ', 'ආ', 'ඇ', 'ඈ', 'ඉ', 'ඊ', 'උ', 'ඌ', 'ඍ', 'ඎ', 'එ', 'ඒ', 'ඓ', 'ඔ', 'ඕ', 'ඖ',
            ]
        }
    },

    # Swaradesha Sandhi
    {
        'P': 'Pattern-O4',
        'L': {
            'C': [
                'ක්', 'ඛ්', 'ග්', 'ඝ්', 'ඞ්', 'ඟ්', 'ච්', 'ඡ්', 'ජ්', 'ඣ්', 'ඤ්', 'ඦ්',
                'ට්', 'ඨ්', 'ඩ්', 'ඪ්', 'ණ්', 'ඬ්', 'ත්', 'ථ්', 'ද්', 'ධ්', 'න්', 'ඳ්',
                'ප්', 'ඵ්', 'බ්', 'භ්', 'ම්', 'ඹ්', 'ය්', 'ර්', 'ල්', 'ව්',
                'ශ්', 'ෂ්', 'ස්', 'හ්', 'ළ්', 'ෆ්'
            ],
            'V': ['අ']
        },
        'R': {
            'C': [None],
            'V': ['ඉ']
        },
        'I': {
            'C': None,
            'V': 'එ'
        }
    },
    {
        'P': 'Pattern-O4',
        'L': {
            'C': [
                'ක්', 'ඛ්', 'ග්', 'ඝ්', 'ඞ්', 'ඟ්', 'ච්', 'ඡ්', 'ජ්', 'ඣ්', 'ඤ්', 'ඦ්',
                'ට්', 'ඨ්', 'ඩ්', 'ඪ්', 'ණ්', 'ඬ්', 'ත්', 'ථ්', 'ද්', 'ධ්', 'න්', 'ඳ්',
                'ප්', 'ඵ්', 'බ්', 'භ්', 'ම්', 'ඹ්', 'ය්', 'ර්', 'ල්', 'ව්',
                'ශ්', 'ෂ්', 'ස්', 'හ්', 'ළ්', 'ෆ්'
            ],
            'V': ['අ']
        },
        'R': {
            'C': [None],
            'V': ['උ']
        },
        'I': {
            'C': None,
            'V': 'ඔ'
        }
    },
    {
        'P': 'Pattern-O4',
        'L': {
            'C': [
                'ක්', 'ඛ්', 'ග්', 'ඝ්', 'ඞ්', 'ඟ්', 'ච්', 'ඡ්', 'ජ්', 'ඣ්', 'ඤ්', 'ඦ්',
                'ට්', 'ඨ්', 'ඩ්', 'ඪ්', 'ණ්', 'ඬ්', 'ත්', 'ථ්', 'ද්', 'ධ්', 'න්', 'ඳ්',
                'ප්', 'ඵ්', 'බ්', 'භ්', 'ම්', 'ඹ්', 'ය්', 'ර්', 'ල්', 'ව්',
                'ශ්', 'ෂ්', 'ස්', 'හ්', 'ළ්', 'ෆ්'
            ],
            'V': ['අ']
        },
        'R': {
            'C': [None],
            'V': ['උ']
        },
        'I': {
            'C': None,
            'V': 'ඕ'
        }
    },
    {
        'P': 'Pattern-O4',
        'L': {
            'C': [
                'ක්', 'ඛ්', 'ග්', 'ඝ්', 'ඞ්', 'ඟ්', 'ච්', 'ඡ්', 'ජ්', 'ඣ්', 'ඤ්', 'ඦ්',
                'ට්', 'ඨ්', 'ඩ්', 'ඪ්', 'ණ්', 'ඬ්', 'ත්', 'ථ්', 'ද්', 'ධ්', 'න්', 'ඳ්',
                'ප්', 'ඵ්', 'බ්', 'භ්', 'ම්', 'ඹ්', 'ය්', 'ර්', 'ල්', 'ව්',
                'ශ්', 'ෂ්', 'ස්', 'හ්', 'ළ්', 'ෆ්'
            ],
            'V': ['එ']
        },
        'R': {
            'C': [None],
            'V': ['අ']
        },
        'I': {
            'C': None,
            'V': 'ඈ'
        }
    },

    # svara sandhi - svarṇa svara dīrghaya
    {
        'P': 'Pattern-O4',
        'L': {
            'C': [
                'ක්', 'ඛ්', 'ග්', 'ඝ්', 'ඞ්', 'ඟ්', 'ච්', 'ඡ්', 'ජ්', 'ඣ්', 'ඤ්', 'ඦ්',
                'ට්', 'ඨ්', 'ඩ්', 'ඪ්', 'ණ්', 'ඬ්', 'ත්', 'ථ්', 'ද්', 'ධ්', 'න්', 'ඳ්',
                'ප්', 'ඵ්', 'බ්', 'භ්', 'ම්', 'ඹ්', 'ය්', 'ර්', 'ල්', 'ව්',
                'ශ්', 'ෂ්', 'ස්', 'හ්', 'ළ්', 'ෆ්'
            ],
            'V': ['අ', 'ආ']
        },
        'R': {
            'C': [None],
            'V': ['අ', 'ආ']
        },
        'I': {
            'C': None,
            'V': 'ආ'
        }
    },
    {
        'P': 'Pattern-O4',
        'L': {
            'C': [
                'ක්', 'ඛ්', 'ග්', 'ඝ්', 'ඞ්', 'ඟ්', 'ච්', 'ඡ්', 'ජ්', 'ඣ්', 'ඤ්', 'ඦ්',
                'ට්', 'ඨ්', 'ඩ්', 'ඪ්', 'ණ්', 'ඬ්', 'ත්', 'ථ්', 'ද්', 'ධ්', 'න්', 'ඳ්',
                'ප්', 'ඵ්', 'බ්', 'භ්', 'ම්', 'ඹ්', 'ය්', 'ර්', 'ල්', 'ව්',
                'ශ්', 'ෂ්', 'ස්', 'හ්', 'ළ්', 'ෆ්'
            ],
            'V': ['ඉ', 'ඊ']
        },
        'R': {
            'C': [None],
            'V': ['ඉ', 'ඊ']
        },
        'I': {
            'C': None,
            'V': 'ඊ'
        }
    },
    {
        'P': 'Pattern-O4',
        'L': {
            'C': [
                'ක්', 'ඛ්', 'ග්', 'ඝ්', 'ඞ්', 'ඟ්', 'ච්', 'ඡ්', 'ජ්', 'ඣ්', 'ඤ්', 'ඦ්',
                'ට්', 'ඨ්', 'ඩ්', 'ඪ්', 'ණ්', 'ඬ්', 'ත්', 'ථ්', 'ද්', 'ධ්', 'න්', 'ඳ්',
                'ප්', 'ඵ්', 'බ්', 'භ්', 'ම්', 'ඹ්', 'ය්', 'ර්', 'ල්', 'ව්',
                'ශ්', 'ෂ්', 'ස්', 'හ්', 'ළ්', 'ෆ්'
            ],
            'V': ['උ', 'ඌ']
        },
        'R': {
            'C': [None],
            'V': ['උ', 'ඌ']
        },
        'I': {
            'C': None,
            'V': 'ඌ'
        }
    },

    # svara sandhi - guṇa sandhiya
    {
        'P': 'Pattern-O4',
        'L': {
            'C': [
                'ක්', 'ඛ්', 'ග්', 'ඝ්', 'ඞ්', 'ඟ්', 'ච්', 'ඡ්', 'ජ්', 'ඣ්', 'ඤ්', 'ඦ්',
                'ට්', 'ඨ්', 'ඩ්', 'ඪ්', 'ණ්', 'ඬ්', 'ත්', 'ථ්', 'ද්', 'ධ්', 'න්', 'ඳ්',
                'ප්', 'ඵ්', 'බ්', 'භ්', 'ම්', 'ඹ්', 'ය්', 'ර්', 'ල්', 'ව්',
                'ශ්', 'ෂ්', 'ස්', 'හ්', 'ළ්', 'ෆ්'
            ],
            'V': ['අ', 'ආ']
        },
        'R': {
            'C': [None],
            'V': ['ඉ', 'ඊ']
        },
        'I': {
            'C': None,
            'V': 'එ'
        }
    },
    {
        'P': 'Pattern-O4',
        'L': {
            'C': [
                'ක්', 'ඛ්', 'ග්', 'ඝ්', 'ඞ්', 'ඟ්', 'ච්', 'ඡ්', 'ජ්', 'ඣ්', 'ඤ්', 'ඦ්',
                'ට්', 'ඨ්', 'ඩ්', 'ඪ්', 'ණ්', 'ඬ්', 'ත්', 'ථ්', 'ද්', 'ධ්', 'න්', 'ඳ්',
                'ප්', 'ඵ්', 'බ්', 'භ්', 'ම්', 'ඹ්', 'ය්', 'ර්', 'ල්', 'ව්',
                'ශ්', 'ෂ්', 'ස්', 'හ්', 'ළ්', 'ෆ්'
            ],
            'V': ['අ', 'ආ']
        },
        'R': {
            'C': [None],
            'V': ['උ', 'ඌ']
        },
        'I': {
            'C': None,
            'V': 'ඔ'
        }
    },
    {
        'P': 'Pattern-O5',
        'L': {
            'C': [
                'ක්', 'ඛ්', 'ග්', 'ඝ්', 'ඞ්', 'ඟ්', 'ච්', 'ඡ්', 'ජ්', 'ඣ්', 'ඤ්', 'ඦ්',
                'ට්', 'ඨ්', 'ඩ්', 'ඪ්', 'ණ්', 'ඬ්', 'ත්', 'ථ්', 'ද්', 'ධ්', 'න්', 'ඳ්',
                'ප්', 'ඵ්', 'බ්', 'භ්', 'ම්', 'ඹ්', 'ය්', 'ර්', 'ල්', 'ව්',
                'ශ්', 'ෂ්', 'ස්', 'හ්', 'ළ්', 'ෆ්'
            ],
            'V': ['අ', 'ආ']
        },
        'R': {
            'C': [None],
            'V': ['ඍ']
        },
        'I': {
            'C': 'ර්',
            'V': 'අ'
        }
    },

    # svara sandhi - vṛddhi sandhiya
    {
        'P': 'Pattern-O4',
        'L': {
            'C': [
                'ක්', 'ඛ්', 'ග්', 'ඝ්', 'ඞ්', 'ඟ්', 'ච්', 'ඡ්', 'ජ්', 'ඣ්', 'ඤ්', 'ඦ්',
                'ට්', 'ඨ්', 'ඩ්', 'ඪ්', 'ණ්', 'ඬ්', 'ත්', 'ථ්', 'ද්', 'ධ්', 'න්', 'ඳ්',
                'ප්', 'ඵ්', 'බ්', 'භ්', 'ම්', 'ඹ්', 'ය්', 'ර්', 'ල්', 'ව්',
                'ශ්', 'ෂ්', 'ස්', 'හ්', 'ළ්', 'ෆ්'
            ],
            'V': ['අ', 'ආ']
        },
        'R': {
            'C': [None],
            'V': ['එ']
        },
        'I': {
            'C': None,
            'V': 'ඓ'
        }
    },
    {
        'P': 'Pattern-O4',
        'L': {
            'C': [
                'ක්', 'ඛ්', 'ග්', 'ඝ්', 'ඞ්', 'ඟ්', 'ච්', 'ඡ්', 'ජ්', 'ඣ්', 'ඤ්', 'ඦ්',
                'ට්', 'ඨ්', 'ඩ්', 'ඪ්', 'ණ්', 'ඬ්', 'ත්', 'ථ්', 'ද්', 'ධ්', 'න්', 'ඳ්',
                'ප්', 'ඵ්', 'බ්', 'භ්', 'ම්', 'ඹ්', 'ය්', 'ර්', 'ල්', 'ව්',
                'ශ්', 'ෂ්', 'ස්', 'හ්', 'ළ්', 'ෆ්'
            ],
            'V': ['අ', 'ආ']
        },
        'R': {
            'C': [None],
            'V': ['ඔ']
        },
        'I': {
            'C': None,
            'V': 'ඖ'
        }
    },

    # svara sandhi - vṛddhi samāhāra sandhiya
    {
        'P': 'Pattern-O4',
        'L': {
            'C': [
                'ක්', 'ඛ්', 'ග්', 'ඝ්', 'ඞ්', 'ඟ්', 'ච්', 'ඡ්', 'ජ්', 'ඣ්', 'ඤ්', 'ඦ්',
                'ට්', 'ඨ්', 'ඩ්', 'ඪ්', 'ණ්', 'ඬ්', 'ත්', 'ථ්', 'ද්', 'ධ්', 'න්', 'ඳ්',
                'ප්', 'ඵ්', 'බ්', 'භ්', 'ම්', 'ඹ්', 'ය්', 'ර්', 'ල්', 'ව්',
                'ශ්', 'ෂ්', 'ස්', 'හ්', 'ළ්', 'ෆ්'
            ],
            'V': ['අ', 'ආ']
        },
        'R': {
            'C': [None],
            'V': ['ඓ']
        },
        'I': {
            'C': None,
            'V': 'ඓ'
        }
    },
    {
        'P': 'Pattern-O4',
        'L': {
            'C': [
                'ක්', 'ඛ්', 'ග්', 'ඝ්', 'ඞ්', 'ඟ්', 'ච්', 'ඡ්', 'ජ්', 'ඣ්', 'ඤ්', 'ඦ්',
                'ට්', 'ඨ්', 'ඩ්', 'ඪ්', 'ණ්', 'ඬ්', 'ත්', 'ථ්', 'ද්', 'ධ්', 'න්', 'ඳ්',
                'ප්', 'ඵ්', 'බ්', 'භ්', 'ම්', 'ඹ්', 'ය්', 'ර්', 'ල්', 'ව්',
                'ශ්', 'ෂ්', 'ස්', 'හ්', 'ළ්', 'ෆ්'
            ],
            'V': ['අ', 'ආ']
        },
        'R': {
            'C': [None],
            'V': ['ඖ']
        },
        'I': {
            'C': None,
            'V': 'ඖ'
        }
    },

    # svara sandhi - ardha svara bhāva sandhiya
    {
        'P': 'Pattern-O6',
        'L': {
            'C': [
                'ක්', 'ඛ්', 'ග්', 'ඝ්', 'ඞ්', 'ඟ්', 'ච්', 'ඡ්', 'ජ්', 'ඣ්', 'ඤ්', 'ඦ්',
                'ට්', 'ඨ්', 'ඩ්', 'ඪ්', 'ණ්', 'ඬ්', 'ත්', 'ථ්', 'ද්', 'ධ්', 'න්', 'ඳ්',
                'ප්', 'ඵ්', 'බ්', 'භ්', 'ම්', 'ඹ්', 'ය්', 'ර්', 'ල්', 'ව්',
                'ශ්', 'ෂ්', 'ස්', 'හ්', 'ළ්', 'ෆ්'
            ],
            'V': ['ඉ', 'ඊ']
        },
        'R': {
            'C': [None],
            'V': ['අ', 'ආ', 'උ', 'ඌ']
        },
        'I': {
            'C': '‍',   # swj
            'V': None,
            'D': 'ය්',
            'W': None
        }
    },
    {
        'P': 'Pattern-O7',
        'L': {
            'C': [
                'ක්', 'ඛ්', 'ග්', 'ඝ්', 'ඞ්', 'ඟ්', 'ච්', 'ඡ්', 'ජ්', 'ඣ්', 'ඤ්', 'ඦ්',
                'ට්', 'ඨ්', 'ඩ්', 'ඪ්', 'ණ්', 'ඬ්', 'ත්', 'ථ්', 'ද්', 'ධ්', 'න්', 'ඳ්',
                'ප්', 'ඵ්', 'බ්', 'භ්', 'ම්', 'ඹ්', 'ය්', 'ර්', 'ල්', 'ව්',
                'ශ්', 'ෂ්', 'ස්', 'හ්', 'ළ්', 'ෆ්'
            ],
            'V': ['ඉ', 'ඊ']
        },
        'R': {
            'C': [None],
            'V': ['එ']
        },
        'I': {
            'C': 'ය්'
        }
    },
    {
        'P': 'Pattern-O7',
        'L': {
            'C': [
                'ක්', 'ඛ්', 'ග්', 'ඝ්', 'ඞ්', 'ඟ්', 'ච්', 'ඡ්', 'ජ්', 'ඣ්', 'ඤ්', 'ඦ්',
                'ට්', 'ඨ්', 'ඩ්', 'ඪ්', 'ණ්', 'ඬ්', 'ත්', 'ථ්', 'ද්', 'ධ්', 'න්', 'ඳ්',
                'ප්', 'ඵ්', 'බ්', 'භ්', 'ම්', 'ඹ්', 'ය්', 'ර්', 'ල්', 'ව්',
                'ශ්', 'ෂ්', 'ස්', 'හ්', 'ළ්', 'ෆ්'
            ],
            'V': ['උ', 'ඌ']
        },
        'R': {
            'C': [None],
            'V': ['අ', 'ආ', 'ඉ', 'ඊ', 'එ', 'ඒ']
        },
        'I': {
            'C': 'ව්'
        }
    },
    {
        'P': 'Pattern-O8',
        'L': {
            'C': [
                'ක්', 'ඛ්', 'ග්', 'ඝ්', 'ඞ්', 'ඟ්', 'ච්', 'ඡ්', 'ජ්', 'ඣ්', 'ඤ්', 'ඦ්',
                'ට්', 'ඨ්', 'ඩ්', 'ඪ්', 'ණ්', 'ඬ්', 'ත්', 'ථ්', 'ද්', 'ධ්', 'න්', 'ඳ්',
                'ප්', 'ඵ්', 'බ්', 'භ්', 'ම්', 'ඹ්', 'ය්', 'ර්', 'ල්', 'ව්',
                'ශ්', 'ෂ්', 'ස්', 'හ්', 'ළ්', 'ෆ්'
            ],
            'V': ['ඍ']
        },
        'R': {
            'C': [None],
            'V': ['අ']
        },
        'I': {
            'C': '‍',   # swj
            'V': 'ර'
        }
    },

    # Gatrādeshạ sandhiya
    {
        'P': 'Pattern-O9',
        'L': {
            'C': [
                'ක්', 'ඛ්', 'ග්', 'ඝ්', 'ඞ්', 'ඟ්', 'ච්', 'ඡ්', 'ජ්', 'ඣ්', 'ඤ්', 'ඦ්',
                'ට්', 'ඨ්', 'ඩ්', 'ඪ්', 'ණ්', 'ඬ්', 'ත්', 'ථ්', 'ද්', 'ධ්', 'න්', 'ඳ්',
                'ප්', 'ඵ්', 'බ්', 'භ්', 'ම්', 'ඹ්', 'ය්', 'ර්', 'ල්', 'ව්',
                'ශ්', 'ෂ්', 'ස්', 'හ්', 'ළ්', 'ෆ්'
            ],
            'V': [None, 'ඉ', 'උ']
        },
        'R': {
            'C': ['ක්'],
            'V': ['අ']
        },
        'I': {
            'C': 'ව්',
        }
    },
    {
        'P': 'Pattern-O9',
        'L': {
            'C': [
                'ක්', 'ඛ්', 'ග්', 'ඝ්', 'ඞ්', 'ඟ්', 'ච්', 'ඡ්', 'ජ්', 'ඣ්', 'ඤ්', 'ඦ්',
                'ට්', 'ඨ්', 'ඩ්', 'ඪ්', 'ණ්', 'ඬ්', 'ත්', 'ථ්', 'ද්', 'ධ්', 'න්', 'ඳ්',
                'ප්', 'ඵ්', 'බ්', 'භ්', 'ම්', 'ඹ්', 'ය්', 'ර්', 'ල්', 'ව්',
                'ශ්', 'ෂ්', 'ස්', 'හ්', 'ළ්', 'ෆ්'
            ],
            'V': ['අ', 'ඉ', 'උ']
        },
        'R': {
            'C': ['ක්'],
            'V': ['අ']
        },
        'I': {
            'C': 'ය්',
        }
    },
    {
        'P': 'Pattern-10',
        'L': {
            'C': ['බ්'],
            'V': ['අ', 'උ']
        },
        'R': {
            'C': ['ප්', 'න්', 'ත්'],
            'V': ['අ', 'ආ', 'ඉ', 'ඔ']
        },
        'I': {
            'C': 'ප්',
        }
    },
    {
        'P': 'Pattern-10',
        'L': {
            'C': ['ද්'],
            'V': ['උ']
        },
        'R': {
            'C': ['බ්', 'ස්'],
            'V': ['අ']
        },
        'I': {
            'C': 'ත්',
        }
    },

]
