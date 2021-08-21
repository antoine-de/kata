import unittest 
import anagram
# # From https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
# import importlib.util
# spec = importlib.util.spec_from_file_location("anagram", "anagram.py")
# foo = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(foo)

class TestAnagram(unittest.TestCase):

    def __init__(self):
        pass

    def test_simple_OK(self):
        anagram = foo.Anagram('ab', '../data/tests/simple_wordlist.txt')
        anagram_list = anagram.find_anagrams()
        self.assertEqual(anagram_list,1)
    
    def test_double_OK(self):
        anagram = Anagram('ab', '../data/tests/double_wordlist.txt')
        anagram_list = anagram.find_anagrams()
        self.assertEqual(anagram_list,2)

    def test_KO(self):
        anagram = Anagram('ab', '../data/tests/no_wordlist.txt')
        anagram_list = anagram.find_anagrams()
        self.assertEqual(anagram_list,0)
