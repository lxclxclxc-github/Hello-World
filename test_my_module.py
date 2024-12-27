# test_my_module.py
import unittest
from my_module import my_function

class TestMyFunction(unittest.TestCase):
    def test_input_200(self):
        self.assertEqual(my_function(200), 500)  # 输入200时，期望返回500

if __name__ == "__main__":
    unittest.main()
