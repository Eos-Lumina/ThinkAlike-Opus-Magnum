import os
import unittest

import src.backend.translation.translation_service as tsvc
from src.backend.translation.translation_service import TranslationService

# Set dummy environment variables for Azure Translator
AZURE_TRANSLATOR_ENDPOINT = "https://fake.cognitiveservices.azure.com/"
os.environ["AZURE_TRANSLATOR_ENDPOINT"] = AZURE_TRANSLATOR_ENDPOINT
AZURE_TRANSLATOR_KEY = "fakeKey"
os.environ["AZURE_TRANSLATOR_KEY"] = AZURE_TRANSLATOR_KEY


# Create a dummy response structure to mock translation
class DummyTranslation:
    def __init__(self, text):
        self.text = text


class DummyResponse:
    def __init__(self, text):
        self.translations = [DummyTranslation(text)]


class DummyClient:
    def __init__(self, endpoint, credential):
        pass

    def translate(self, content, to, from_parameter=None):
        # return dummy response with translated content
        return [DummyResponse(f"[translated to {to[0]}] {content[0]}")]


# Monkey-patch the TextTranslationClient used in TranslationService
tsvc.TextTranslationClient = DummyClient


class TestTranslationService(unittest.TestCase):
    def setUp(self):
        self.service = TranslationService()

    def test_translate_to_spanish(self):
        text = "Hello, world!"
        translated = self.service.translate(text, "es")
        self.assertTrue(translated.startswith("[translated to es]"))


if __name__ == "__main__":
    unittest.main()
