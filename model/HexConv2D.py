import numpy as np
from torch import nn

from abalone import AbaloneModel


class HexConv2DLayer(nn.Module):

    def __init__(self, kernel_size, edge_size, dilation=1, padding=0, stride=1, shuffle=True):
        super(HexConv2DLayer, self).__init__()
        self.kernel_size = kernel_size
        self.edge_size = edge_size
        self.dilation = dilation
        self.padding = padding
        self.stride = stride
        self.shuffle = shuffle

        self.kernel = self._build_kernel()

        self.get_1d_pos, _ = AbaloneModel.build_indexed_pos_method(edge_size)

    def _build_kernel(self) -> np.ndarray:
        pass

    # Pytorch

    def forward(self, x):
        return x
