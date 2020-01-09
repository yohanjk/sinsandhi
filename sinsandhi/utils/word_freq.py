import itertools
import os
import re

from nltk import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from tqdm import tqdm

symbols = [
    '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=',
    ',', '<', '.', '>', '/', '?', ';', ':', '"', '"', '[', '{', ']', '}', '|',
    '´´', '–', '‘', '’', '“', '”', '•', '', '', '±', '»', '¼', '½', '.', '-', '.', ','
]


def create_word_freq_dic(text_file_path, freq_dic_path='freq_dic.txt'):
    freq = FreqDist()

    try:
        with tqdm(total=os.path.getsize(text_file_path)) as pbar:
            with open(text_file_path) as file:
                for line in file:
                    pbar.update(len(line.encode('utf-8')))
                    tmp_l = line
                    for s in symbols:
                        tmp_l = tmp_l.replace(s, ' ')
                    tmp_l = re.sub(r'\d', '#', tmp_l)
                    tmp_l = re.sub(r'#*#', '#', tmp_l)
                    words = list(itertools.chain.from_iterable(map(word_tokenize, sent_tokenize(tmp_l))))
                    freq.update(words)
                file.close()
    except IOError:
        print('Error while reading text file')
        print('Specified File: ', text_file_path, ' is not accessible')
        exit()

    freq = dict(freq)

    for k in symbols:
        freq.pop(k, None)

    with open(freq_dic_path, 'w') as freq_output:
        for k, v in sorted(freq.items()):
            freq_output.write(f'{k} {v}\n')
        freq_output.close()


def read_freq_dic(freq_dic_path):
    freq = {}

    try:
        with open(freq_dic_path) as file:
            for line in file:
                data = line.split()
                if len(data) == 2:
                    freq[data[0]] = data[1]

    except IOError:
        print('Error while reading frequency dictionary')
        print('Specified File: ', freq_dic_path, ' is not accessible')
        exit()

    return freq
