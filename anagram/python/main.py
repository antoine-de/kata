import copy

WORD = 'documenting'
WORDLIST_PATH = '../data/test_wordlist.txt'
WORDLIST_PATH = '../data/wordlist.txt'

def decompose_word():
    letter_dict={}
    for letter in WORD:
        if letter not in letter_dict.keys():
            letter_dict[letter]=1
        else:
            letter_dict[letter]+=1
    return letter_dict

def load_wordlist():
    wordlist=[]
    f = open(WORDLIST_PATH, 'r')
    lines = f.readlines()[1:]
    for line in lines:
        wordlist += line.split()
    return wordlist

def print_anagram(letter_dict, concatenated_word):
    if check_words(letter_dict, concatenated_word):
        print(concatenated_word + ' is an anagram of ' + WORD)
    
    
def check_words(letter_dict, concatenated_word):
    other_letter_dict = copy.deepcopy(letter_dict)
    for letter in concatenated_word:
        if letter not in other_letter_dict:
            return False
        if not check_occurence(other_letter_dict, letter):
            return False
    return True

def check_occurence(letter_dict, letter):
    if letter_dict[letter]>0:
        letter_dict[letter]-=1
        return True
    return False

def search_anagrams(letter_dict):
    index_word = 0
    for word1 in wordlist:
        for word2 in wordlist[index_word:]:
            if len(word1) + len(word2) == len(WORD):
                concatenated_word = word1 + word2
                print_anagram(letter_dict, concatenated_word)
        index_word += 1

if __name__ == "__main__":
    wordlist = load_wordlist()
    letter_dict = decompose_word()
    search_anagrams(letter_dict)
