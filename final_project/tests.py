import unittest
from translator import english_to_french, french_to_english

class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Monday'), 'Lundi') 
    def test2(self):    
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def test3(self):    
        self.assertEqual(english_to_french(''), 'Input is null') 
    def test4(self):    
        self.assertEqual(english_to_french('Sky'), 'Ciel')             

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Pomme'), 'Apple') 
    def test2(self):    
        self.assertEqual(french_to_english('Porte'), 'Door')
    def test3(self):    
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    def test4(self):    
        self.assertEqual(french_to_english(''), 'Input is null')      


unittest.main()
