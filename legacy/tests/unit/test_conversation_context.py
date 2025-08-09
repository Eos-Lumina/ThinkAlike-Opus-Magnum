import unittest
from agent_framework.framework.utils.conversation_context import ConversationContext

class TestConversationContext(unittest.TestCase):
    def setUp(self):
        self.ctx = ConversationContext("test_ctx")

    def test_add_and_get_message(self):
        self.ctx.add_message("user1", "Hello!")
        self.ctx.add_message("user2", "Hi!")
        history = self.ctx.get_history()
        self.assertEqual(len(history), 2)
        self.assertEqual(history[0].content, "Hello!")
        self.assertEqual(history[1].content, "Hi!")

    def test_metadata(self):
        self.ctx.set_metadata("topic", "test")
        self.assertEqual(self.ctx.get_metadata("topic"), "test")

    def test_custom_attributes(self):
        self.ctx.set_attribute("foo", "bar")
        self.assertEqual(self.ctx.get_attribute("foo"), "bar")

    def test_clear_history(self):
        self.ctx.add_message("user1", "Hello!")
        self.ctx.clear_history()
        self.assertEqual(len(self.ctx.get_history()), 0)

if __name__ == "__main__":
    unittest.main()
