import unittest

from abalone import FieldTemplate, AbaloneModel

model3 = AbaloneModel.AbaloneAgent(edge_size=3, vector_generator=FieldTemplate.basic_start)
model5 = AbaloneModel.AbaloneAgent(edge_size=5, vector_generator=FieldTemplate.basic_start)
model10 = AbaloneModel.AbaloneAgent(edge_size=10, vector_generator=FieldTemplate.basic_start)


class TestHexConv2D(unittest.TestCase):

    def test_hex_conv_pth2(self):
        pass

    def test_hex_conv_pth3(self):
        pass

    def test_hex_conv_pth4(self):
        pass

    def test_hex_conv_pth5(self):
        pass

    def test_forward_model(self):
        pass

    def test_backward_model(self):
        pass
