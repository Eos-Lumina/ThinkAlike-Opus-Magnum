import unittest

from src.backend.voice.invoke_service import VoiceInvokeService


class TestVoiceInvokeService(unittest.TestCase):
    def setUp(self):
        self.service = VoiceInvokeService()
        self.wakephrases = ["Eos Illuminate", "ThinkAlike Activate"]

    def test_detect_wakephrase_found(self):
        transcript = "Eos Illuminate the path forward"
        detected = self.service.detect_wakephrase(transcript, self.wakephrases)
        self.assertTrue(detected)

    def test_detect_wakephrase_not_found(self):
        transcript = "Hello world"
        detected = self.service.detect_wakephrase(transcript, self.wakephrases)
        self.assertFalse(detected)

    def test_transcribe_placeholder(self):
        # Since transcribe is a placeholder, it should return an empty string
        transcript = self.service.transcribe("dummy_path.wav")
        self.assertEqual(transcript, "")


if __name__ == "__main__":
    unittest.main()
