from unittest.mock import Mock
import unittest
from scoreboard import Scoreboard

class TestFile(unittest.TestCase):
    """测试读写最高分如文件的类"""
    def setUp(self):

        mock = Mock()
        self.Scoreboard = Scoreboard(mock)

    def test_write_score(self):
        """测试文件写入，看文件中是否正确写入"""
        self.Scoreboard.prep_score(1500)

    def test_read_score(self):
        """测试从文件中读取最高分的方法"""
        hscore = self.Scoreboard.prep_high_score()
        # 判断从读取的值是否是文件中的预期值
        self.assertEqual(1500, hscore)

if __name__ == '__main__':
    unittest.main()
