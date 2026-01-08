import unittest
import random
from nails_roulette import COLORS, SHAPES, DECORATIONS

class TestNailRoulette(unittest.TestCase):
    def test_spin_color(self):
        color = random.choice(COLORS)
        self.assertIn(color, COLORS)

    def test_spin_shape(self):
        shape = random.choice(SHAPES)
        self.assertIn(shape, SHAPES)

    def test_spin_deco(self):
        deco = random.choice(DECORATIONS)
        self.assertIn(deco, DECORATIONS)

    def test_add_new_color(self):
        COLORS.append("Test Color")
        self.assertIn("Test Color", COLORS)
        COLORS.remove("Test Color")

    def test_add_new_shape(self):
        SHAPES.append("Test Shape")
        self.assertIn("Test Shape", SHAPES)
        SHAPES.remove("Test Shape")

    def test_add_new_deco(self):
        DECORATIONS.append("Test Deco")
        self.assertIn("Test Deco", DECORATIONS)
        DECORATIONS.remove("Test Deco")

if __name__ == "__main__":
    unittest.main()
