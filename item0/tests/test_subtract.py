import unittest
from example import subtract

# 编写一个测试类，继承自 unittest.TestCase
class TestSubtractunction(unittest.TestCase):
    
    # 定义测试函数，名称以 test_ 开头
    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(3, 2), 1)
    
    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-1, -2), 1)
    
    def test_subtract_mixed_numbers(self):
        self.assertEqual(subtract(10, -5), 15)

# 如果这个脚本被直接运行，执行测试
if __name__ == '__main__':
    unittest.main()
