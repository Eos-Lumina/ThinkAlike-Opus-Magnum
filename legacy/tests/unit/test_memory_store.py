import unittest
from agent_framework.framework.utils.memory_store import MemoryStore

class TestMemoryStore(unittest.TestCase):
    def setUp(self):
        self.memory = MemoryStore()

    def test_set_and_get(self):
        self.memory.set("foo", "bar")
        self.assertEqual(self.memory.get("foo"), "bar")

    def test_delete_and_has(self):
        self.memory.set("foo", "bar")
        self.memory.delete("foo")
        self.assertFalse(self.memory.has("foo"))

    def test_clear(self):
        self.memory.set("foo", "bar")
        self.memory.clear()
        self.assertEqual(self.memory.get_all(), {})

if __name__ == "__main__":
    unittest.main()
