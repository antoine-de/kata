import copy

class Anagram():
    def __init__(self, word, word_list_path):
        self.WORD = word
        self.WORDLIST_PATH = word_list_path

    def find_anagrams(self):
        wordlist = self.load_wordlist()
        letter_dict = self.decompose_word()
        self.search_anagrams(letter_dict, wordlist)

    def decompose_word(self):
        letter_dict={}
        for letter in self.WORD:
            if letter not in letter_dict.keys():
                letter_dict[letter]=1
            else:
                letter_dict[letter]+=1
        return letter_dict

    def load_wordlist(self):
        wordlist=[]
        f = open(self.WORDLIST_PATH, 'r')
        lines = f.readlines()[1:]
        for line in lines:
            wordlist += line.split()
        return wordlist

    def print_anagram(self, letter_dict, concatenated_word):
        if self.check_words(letter_dict, concatenated_word):
            print(concatenated_word + ' is an anagram of ' + self.WORD)
        
        
    def check_words(self, letter_dict, concatenated_word):
        other_letter_dict = copy.copy(letter_dict)
        for letter in concatenated_word:
            if letter not in other_letter_dict:
                return False
            if not self.check_occurence(other_letter_dict, letter):
                return False
        return True

    def check_occurence(self, letter_dict, letter):
        if letter_dict[letter]>0:
            letter_dict[letter]-=1
            return True
        return False

    def search_anagrams(self, letter_dict, wordlist):
        index_word = 0
        for word1 in wordlist:
            for word2 in wordlist[index_word:]:
                if len(word1) + len(word2) == len(self.WORD):
                    concatenated_word = word1 + word2
                    self.print_anagram(letter_dict, concatenated_word)
            index_word += 1
