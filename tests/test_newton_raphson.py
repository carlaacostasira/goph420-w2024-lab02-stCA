import unittest
import numpy as np
from goph420_lab02.root_finding import root_newton_raphson

class TestNewtonRaphson1(unittest.TestCase):
    def setUp(self):
        self.f = lambda x0: x0**2 - 1
        self.dfdx = lambda x0: 2*x0
        
    def test_newton_raphson(self):
        self.x0 = 1.5
        estimation = root_newton_raphson(self.x0,self.f,self.dfdx)
        actual = 1
        self.assertAlmostEqual(estimation[0], actual)
        
class TestNewtonRaphson2(unittest.TestCase): 
    def setUp(self):
        self.f = lambda x0: np.sin(x0)
        self.dfdx = lambda x0: np.cos(x0)
        
    def test_newton_raphson(self):
        self.x0 = 3*(np.pi)/4
        estimation = root_newton_raphson(self.x0,self.f,self.dfdx)
        actual = np.pi
        self.assertAlmostEqual(estimation[0], actual)

if __name__ == '__main__':
    unittest.main()