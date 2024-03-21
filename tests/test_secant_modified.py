import unittest
import numpy as np
from goph420_lab02.root_finding import root_secant_modified

class TestSecantModified(unittest.TestCase):
    def setUp(self):
        self.x0 = 2
        self.dx = ???????
        self.f = 2*self.x0**2 + 3
        
    def test_secant_modified(self):
        estimation = root_secant_modified(self.x0,self.dx,self.f)
        