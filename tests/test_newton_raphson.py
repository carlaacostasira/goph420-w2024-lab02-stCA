import unittest
import numpy as np
from goph420_lab02.root_finding import root_newton_raphson

class TestNewtonRaphson(unittest.TestCase):
    def setUp(self):
        self.x0 = 2
        self.f = 2*self.x0**2 + 3
        self.dfdx = 4*self.x0
        
    def test_newton_raphson(self):
        estimation = root_newton_raphson(self.x0,self.f,self.dfdx)

