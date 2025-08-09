import unittest
from agent_framework.framework.utils.persona_utils import load_persona, apply_persona_to_response

class TestPersonaUtils(unittest.TestCase):
    def test_load_persona(self):
        persona = load_persona("neutral_assistant")
        self.assertIn("greeting", persona)
        self.assertEqual(persona["response_style"], "formal")
        persona2 = load_persona("friendly_chat_buddy")
        self.assertIn("greeting", persona2)
        self.assertEqual(persona2["response_style"], "informal")
        persona3 = load_persona("unknown")
        self.assertIn("error", persona3)

    def test_apply_persona_to_response(self):
        persona = load_persona("neutral_assistant")
        response = apply_persona_to_response("hello there", persona)
        self.assertEqual(response, "Hello there")
        persona2 = load_persona("friendly_chat_buddy")
        response2 = apply_persona_to_response("HELLO THERE", persona2)
        self.assertEqual(response2, "hello there")

if __name__ == "__main__":
    unittest.main()
