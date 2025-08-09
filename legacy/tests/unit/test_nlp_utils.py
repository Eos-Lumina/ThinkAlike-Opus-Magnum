import unittest
from agent_framework.framework.utils.nlp_utils import basic_tokenize, detect_intent

class TestNLPUtils(unittest.TestCase):
    def test_basic_tokenize(self):
        tokens = basic_tokenize("Hello World!")
        self.assertEqual(tokens, ["hello", "world!"])

    def test_detect_intent(self):
        self.assertEqual(detect_intent("Hello there!"), "greeting")
        self.assertEqual(detect_intent("Bye now!"), "farewell")
        self.assertEqual(detect_intent("What's up?"), "unknown")

if __name__ == "__main__":
    unittest.main()
