import os
import pickle

from statistics import harmonic_mean

from sinsandhi.joiner import join_words
from sinsandhi.splitter import split_word
from sinsandhi.utils.word_freq import read_freq_dic


class SandhiTool:

    def __init__(self, wfd_path=None):
        """

        :param wfd_path: path to word frequency dictionary file
        """
        if wfd_path is not None:
            self.freq_dic = read_freq_dic(wfd_path)
        else:
            self.freq_dic = {}

    def join(self, l, r):
        """

        :param l: left word
        :param r: right word
        :return: dictionary {'best': x, output:{all possible outputs}}
        """
        words = join_words(l, r)
        if len(words) > 0:
            output = {}
            for word in words:
                if word in self.freq_dic:
                    output[word] = self.freq_dic[word]
                else:
                    output[word] = 0
            output = sorted(output.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
            output = dict(output)
            return {
                'best': next(iter(output)),
                'output': output
            }
        else:
            return None

    def split(self, w):
        splits = split_word(w)
        if len(splits):
            output = {}
            for l_word, r_word in splits:
                lf = 0 if l_word not in self.freq_dic else self.freq_dic[l_word]
                rf = 0 if r_word not in self.freq_dic else self.freq_dic[r_word]
                score = harmonic_mean([lf, rf])
                output[(l_word, r_word)] = score
            output = sorted(output.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
            output = dict(output)
            return {
                'best': next(iter(output)),
                'output': output
            }
        else:
            return None
