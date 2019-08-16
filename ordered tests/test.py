import unittest
from stack import Stack


class StackTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Stack()

    def get_items(self, reverse=False):
        items = [2, 5, 1, 4, 7]
        if reverse:
            items.reverse()
        return items

    def step1(self):
        items = self.get_items()
        for item in items:
            self.s.push(item)
            self.assertEqual(item, self.s.peek())

    def step2(self):
        items = self.get_items(True)
        for item in items:
            self.assertEqual(item, self.s.pop())

    def step3(self):
        self.assertEqual(0, len(self.s))

    def _steps(self):
        for name in sorted(dir(self)):
            if name.startswith("step"):
                yield name, getattr(self, name)

    def test_steps(self):
        for name, step in self._steps():
            try:
                step()
            except Exception as e:
                self.fail("{} failed ({}: {})".format(step, type(e), e))
