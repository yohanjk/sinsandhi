import sinsandhi.utils.letters as letters


def process_string(string):
    string = string.strip()
    length = len(string)
    start = 0
    char_list = []
    if string[0] in letters.VOWELS:
        char_list.append(None)
        char_list.append(string[0])
        start = 1
    for i in range(start, length):
        if string[i] in letters.VOWEL_DIACRITICS:
            char_list.append(letters.VOWEL_REVERSE_DIACRITICS_MAPPING[string[i]])
        elif string[i] == '්':
            char_list.append(None)
        elif ord(string[i]) == 8205:
            char_list.append(string[i])
            char_list.append(None)
        elif string[i] == 'ර' and ord(string[i-1]) == 8205:
            del char_list[-1]
            char_list.append('ර')
        elif string[i] in ['ං', 'ඃ']:
            char_list.append(string[i])
            char_list.append(None)
        else:
            char_list.append(string[i] + '්')
            if i + 1 < length:
                if string[i + 1] in letters.BASE_CONSONANTS:
                    char_list.append('අ')
            else:
                char_list.append('අ')
    return char_list


def convert_to_string(char_list):
    string = ''
    start = 0
    if char_list[0] is None:
        string = string + char_list[1]
        start = 2
    for i in range(start, len(char_list)):
        if char_list[i] is not None:
            if char_list[i] in letters.CONSONANTS:
                if char_list[i+1] is not None:
                    string = string + char_list[i][0]
                else:
                    string = string + char_list[i]
            elif char_list[i] in letters.VOWELS:
                string = string + letters.VOWEL_DIACRITICS_MAPPING[char_list[i]]
            else:
                # ord(char_list[i]) == 8205:
                string = string + char_list[i]
        else:
            pass
    return string

