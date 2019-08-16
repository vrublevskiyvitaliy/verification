import unittest
from main import Solution
from ddt import ddt, data, unpack


@ddt
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

    @data(
        ('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"], 5),
        ('hit', 'cog', ["hot", "dot", "dog", "lot", "log"], 0),
        ('hit', 'hot', ["hot", "dot", "dog", "lot", "log"], 2),
        ('', '', ["hot", "dot", "dog", "lot", "log"], 0),
        ('12', '132', ["hot", "dot", "dog", "lot", "log"], 0),
        ('hit', 'cog', [], 0),
    )
    @unpack
    def test_first(self, begin_word, end_word, word_list, answer):
        self.assertEqual(answer, self.solution.ladderLength(begin_word, end_word, word_list))
