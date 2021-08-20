import anagram

WORD = 'documenting'
WORDLIST_PATH = '../data/wordlist.txt'

if __name__ == "__main__":
    myAnagram = anagram.Anagram(WORD, WORDLIST_PATH)
    myAnagram.find_anagrams()
