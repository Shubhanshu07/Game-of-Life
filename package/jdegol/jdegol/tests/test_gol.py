import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from jdegol.gol import * 

class TestUM(unittest.TestCase): 
    def setUp(self):
        pass
 
    def test_pg_from_json(self):
        expected_result = [
            [1,1,1,1,1,1],
            [1,1,0,0,0,1],
            [1,0,1,0,0,1],
            [1,0,0,1,0,1],
            [1,0,0,0,1,1],
            [1,1,1,1,1,1]
        ]
        self.assertEqual(pg_from_json(json_path="jdegol/tests/sample.json"), expected_result)
 
    def test_gen_rand_pg(self):
        height = 20
        width = 20

        generated_pg = gen_rand_pg(h=height, w=width)

        self.assertEqual(len(generated_pg), height)
        for row in generated_pg:
            self.assertEqual(len(row), width)

    def test_update_pg(self):
        initial_config = [
            [1,1,1,1,1,1],
            [1,1,0,0,0,1],
            [1,0,1,0,0,1],
            [1,0,0,1,0,1],
            [1,0,0,0,1,1],
            [1,1,1,1,1,1]
        ]

        expected_final_config = [
            [1,0,1,1,1,1],
            [0,0,0,0,0,1],
            [1,0,1,0,0,1],
            [1,0,0,1,0,1],
            [1,0,0,0,0,0],
            [1,1,1,1,0,1]
        ]

        self.assertEqual(expected_final_config, update_pg(initial_config))

    def test_get_neighbours(self):
        initial_config = [
            [1,1,1,1,1,1],
            [1,1,0,0,0,1],
            [1,0,1,0,0,1],
            [1,0,0,1,0,1],
            [1,0,0,0,1,1],
            [1,1,1,1,1,1]
        ]

        result = get_neighbours(initial_config)

        expected_result = [
            [3, 4, 3, 2, 3, 2],
            [4, 6, 5, 4, 5, 3],
            [3, 5, 2, 2, 4, 2],
            [2, 4, 2, 2, 5, 3],
            [3, 5, 4, 5, 6, 4],
            [2, 3, 2, 3, 4, 3]
        ]

        self.assertEqual(expected_result, result)
    
if __name__ == '__main__':
    unittest.main()
