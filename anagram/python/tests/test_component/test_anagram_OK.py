import unittest 
import sys
sys.path.append('../../')
sys.path.append('./')
from anagram import Anagram

# # From https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
# import importlib.util
# spec = importlib.util.spec_from_file_location("anagrams", "anagrams.py")
# foo = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(foo)

class Testanagrams(unittest.TestCase):


    def test_simple_OK(self):
        anagrams = Anagram('ab', '../data/tests/simple_wordlist.txt')
        anagrams_list = anagrams.find_anagrams()
        self.assertEqual(anagrams_list, ['ab'])
    
    def test_double_OK(self):
        anagrams = Anagram('ab', '../data/tests/double_wordlist.txt')
        anagrams_list = anagrams.find_anagrams()
        self.assertEqual(len(anagrams_list), 2)

    def test_KO(self):
        anagrams = Anagram('ab', '../data/tests/no_wordlist.txt')
        anagrams_list = anagrams.find_anagrams()
        self.assertEqual(anagrams_list, [])


if __name__ == '__main__':
    unittest.main()