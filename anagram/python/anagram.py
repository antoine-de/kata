from collections import Counter
import logging
from itertools import combinations

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)
class Anagram():

    def __init__(self, word, word_list_path):
        self.WORD = word
        self.WORDLIST_PATH = word_list_path
        self.WORD_SORTED = sorted(self.WORD.lower())
        self.WORD_COUNTER = Counter(self.WORD.lower())

    def find_anagrams(self):
        letter_dict = self.decompose_word()
        wordlist = self.load_wordlist(letter_dict)

        return self.search_anagrams(letter_dict, wordlist)

    def decompose_word(self):
        letter_dict = {}
        for letter in self.WORD:
            if letter not in letter_dict.keys():
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1
        return letter_dict

    def load_wordlist(self,letter_dict):
        LOGGER.info('Loading word list.')
        wordlist = []
        f = open(self.WORDLIST_PATH, 'r')
        lines = f.readlines()
        for line in lines:
            if (not line.startswith('#')) and self.check_letters(line.replace('\n','').lower(), letter_dict):
                wordlist.extend(line.split())
        return wordlist
    
    def check_letters(self, word, letter_dict):
        for letter in word:
            if letter not in letter_dict.keys():
                return False
        return True

    def check_words(self, letter_dict, concatenated_word):
        other_letter_dict = {}
        for letter in concatenated_word:
            if letter not in letter_dict.keys():
                return False
            if letter in other_letter_dict.keys():
                other_letter_dict[letter] += 1
            else:
                other_letter_dict[letter] = 1
        return letter_dict == other_letter_dict

    # def check_occurence(self, letter_dict, letter):
    #     if letter_dict[letter] > 0:
    #         letter_dict[letter] -= 1
    #         return True
    #     return False

    def search_anagrams(self, letter_dict, wordlist):
        LOGGER.info('Searching anagram.')
        anagram_list = []
        for word1, word2 in combinations(wordlist, 2):
            if len(word1 + word2) == len(self.WORD) and \
                self.check_words(letter_dict, word1 + word2):
                    # Counter(word1 + word2) == self.WORD_COUNTER:
                    # sorted(word1 + word2) == self.WORD_SORTED:
                print(word1 + ' & ' + word2 +
                        ' are an anagram of ' + self.WORD)
                anagram_list.append(word1+word2)
        return anagram_list
