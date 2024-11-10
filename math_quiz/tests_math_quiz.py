import unittest
from math_quiz import random_integer, random_operator, calculate_result


class TestMathGame(unittest.TestCase):

    def test_function_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_random_operator(self):
                
        for _ in range(1000)
            operator = random_operator()
            # Test if generated operator is valid one 
            operator_accepted = (operator == '+') or (operator == '-') or (operator == '*')
            self.assertTrue(operator_accepted)
        

    def test_function_calculate_result(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7), (3, 2, '-', '3 - 2', 1),
                (4, 8, '+', '4 + 8', 12), (3, 6, '*', '3 * 6', 18),
                (5, 4, '+', '5 + 4', 9), (7, 6, '-', '7 - 6', 1),
                (6, 2, '*', '6 * 2', 12), (6, 5, '-', '8 - 5', 3),
                (1, 6, '*', '1 * 6', 6), (4, 6, '*', '4 * 6', 24),
                (7, 9, '*', '7 * 9', 63), (8, 6, '*', '8 * 6', 48)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # insert num1, num2, operator into calculation
                p,a = calculate_result(num1,num2, operator)
                # check expected answer and expected problem
                self.assertTrue(p == expected_problem)
                self.assertTrue(a == expected_answer)
            

if __name__ == "__main__":
    unittest.main()