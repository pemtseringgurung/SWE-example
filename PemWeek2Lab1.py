import unittest

class Parent:
    def multiply(self, x):
        return x * 2 

    def division(self, x):
        return x / 2 

    def addition(self, x):
        return x + 10

class Child(Parent):
    pass

class TestMultiply(unittest.TestCase):

    def test_multiply(self):
        child_instance = Child()
        self.assertEqual(child_instance.multiply(5), 10)  

    def test_multiply_again(self):
        child_instance_second = Child()
        self.assertEqual(child_instance_second.multiply(8), 16)  

    def test_division(self):
        child_instance_third = Child()
        self.assertEqual(child_instance_third.division(12),6)


    def test_addtion(self):
        child_instance_fifth = Child()
        self.assertEqual(child_instance_fifth.addition(1),11)

    def test_addition_again(self):
        child_instance_sixth = Child()
        self.assertEqual(child_instance_sixth.addition(10),20)

if __name__ == '__main__':
    unittest.main()