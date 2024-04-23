import unittest
from example import add

# 编写一个测试类，继承自 unittest.TestCase
class TestAddFunction(unittest.TestCase):
    
    # 定义测试函数，名称以 test_ 开头
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)
    
    def test_add_mixed_numbers(self):
        self.assertEqual(add(10, -5), 5)

# 如果这个脚本被直接运行，执行测试
if __name__ == '__main__':
    unittest.main()
