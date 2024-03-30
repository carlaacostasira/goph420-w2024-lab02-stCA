import unittest
import numpy as np
from goph420_lab02.root_finding import root_secant_modified

class TestSecantModified1(unittest.TestCase):
    def setUp(self):
        self.f = lambda x0: 2*x0 - 1
        
    def test_secant_modified(self):
        self.x0 = 1.0
        self.dx = 0.5
        estimation = root_secant_modified(self.x0,self.dx,self.f)
        actual = 0.5
        self.assertAlmostEqual(estimation[0], actual)

class TestSecantModified2(unittest.TestCase): 
    def setUp(self):
        self.f = lambda x0: np.sin(x0)
        
    def test_secant_modified(self):
        self.x0 = 3*(np.pi)/4
        self.dx = 0.1
        estimation = root_secant_modified(self.x0,self.dx,self.f)
        actual = np.pi
        self.assertAlmostEqual(estimation[0], actual)
        
if __name__ == '__main__':
    unittest.main()