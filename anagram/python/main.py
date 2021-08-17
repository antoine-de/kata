import anagram

WORD = 'documenting'
WORDLIST_PATH = '../data/test_wordlist.txt'
WORDLIST_PATH = '../data/wordlist.txt'

if __name__ == "__main__":
    anagram = anagram.Anagram(WORD, WORDLIST_PATH)
    anagram.find_anagrams()