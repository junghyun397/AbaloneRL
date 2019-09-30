from torch import nn

from abalone import AbaloneModel


class HexConv2DLayer(nn.Module):

    def __init__(self, kernel_size, edge_size, dilation=1, padding=0, stride=1, shuffle=True):
        super(HexConv2DLayer, self).__init__()
        self.kernel_size = kernel_size
        self.edge_size = edge_size

        self.padding = padding
        self.stride = stride
        self.shuffle = shuffle
        self.unfold = nn.Unfold(kernel_size, dilation, padding, stride)

        self.get_1d_pos, _ = AbaloneModel.build_indexed_pos_method(edge_size)

    def forward(self, x):
        pass
