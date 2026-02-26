# test_ollamacipher.py
"""
Tests for OllamaCipher module.
"""

import unittest
from ollamacipher import OllamaCipher

class TestOllamaCipher(unittest.TestCase):
    """Test cases for OllamaCipher class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OllamaCipher()
        self.assertIsInstance(instance, OllamaCipher)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OllamaCipher()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
