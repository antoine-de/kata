import copy


class Anagram():
    def __init__(self, word, word_list_path):
        self.WORD = word
        self.WORDLIST_PATH = word_list_path

    def find_anagrams(self):
        wordlist = self.load_wordlist()
        letter_dict = self.decompose_word()
        return self.search_anagrams(letter_dict, wordlist)

    def decompose_word(self):
        letter_dict = {}
        for letter in self.WORD:
            if letter not in letter_dict.keys():
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1
        return letter_dict

    def load_wordlist(self):
        wordlist = []
        f = open(self.WORDLIST_PATH, 'r')
        lines = f.readlines()
        for line in lines:
            if not line.startswith('#'):
                wordlist.extend(line.split())
        return wordlist

        
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

    def check_occurence(self, letter_dict, letter):
        if letter_dict[letter] > 0:
            letter_dict[letter] -= 1
            return True
        return False

    def search_anagrams(self, letter_dict, wordlist):
        index_word = 0
        anagram_list = []
        for word1 in wordlist:
            for word2 in wordlist[index_word:]:
                if len(word1) + len(word2) == len(self.WORD) and \
                self.check_words(letter_dict, word1 + word2):
                    print(word1 + ' & ' + word2+ ' is an anagram of ' + self.WORD)
                    anagram_list.append(word1+word2)
            index_word += 1
        return anagram_list