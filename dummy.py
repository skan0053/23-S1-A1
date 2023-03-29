from __future__ import annotations
from data_structures.referential_array import ArrayR
from abc import ABC, abstractmethod
from layer_store import LayerStore
from layer_util import Layer, LAYERS, cur_layer_index


class FuckGrid():
    DRAW_STYLE_SET = "SET"
    DRAW_STYLE_ADD = "ADD"
    DRAW_STYLE_SEQUENCE = "SEQUENCE"
    DRAW_STYLE_OPTIONS = (
        DRAW_STYLE_SET,
        DRAW_STYLE_ADD,
        DRAW_STYLE_SEQUENCE
    )

    DEFAULT_BRUSH_SIZE = 2
    MAX_BRUSH = 5
    MIN_BRUSH = 0

    def __init__(self, draw_style, x, y) -> None:
        """
        Initialise the grid object.
        - draw_style:
            The style with which colours will be drawn.
            Should be one of DRAW_STYLE_OPTIONS
            This draw style determines the LayerStore used on each grid square.
        - x, y: The dimensions of the grid.

        Should also intialise the brush size to the DEFAULT provided as a class variable.
        """

        self.draw_style = draw_style
        self.column = x
        self.row = y
        self.brush_size = self.DEFAULT_BRUSH_SIZE

        # 2D Grid
        self.First_dimension = [0,0,0,0]  # -> Array of size 'row' (x)
        print(len(self.First_dimension))  # x = [None,None,None,None]
        self.Second_dimension = [0,0,0,0]
        print(len(self.Second_dimension))   # y = [None,None,None,None]
        # y = [x,x,x,x]
        for i in range(len(self.Second_dimension)):
            self.Second_dimension[i] = [0,0,0,0]
        self.grid_array = self.Second_dimension
        self.grid_array[1][1] = 3
        print(self.grid_array)


if __name__ == "__main__":
    print (LAYERS[0])
    print(LAYERS[1])
    print(LAYERS[2])
    print(LAYERS[3])
    print(LAYERS[4])
    print(LAYERS[5])
    print(LAYERS[6])
    print(LAYERS[7])
    print(LAYERS[8])
    print(cur_layer_index)
    '''
Layer(index=0, apply=<function rainbow at 0x034B1538>, name='rainbow', bg=(200, 0, 120))
Layer(index=1, apply=<function black at 0x0352D3D0>, name='black', bg=(170, 170, 170))
Layer(index=2, apply=<function lighten at 0x0352D418>, name='lighten', bg=(240, 240, 240))
Layer(index=3, apply=<function invert at 0x0352D460>, name='invert', bg=(0, 255, 255))
Layer(index=4, apply=<function red at 0x0352D4A8>, name='red', bg=(255, 0, 0))
Layer(index=5, apply=<function green at 0x0352D4F0>, name='green', bg=(0, 255, 0))
Layer(index=6, apply=<function blue at 0x0352D538>, name='blue', bg=(0, 0, 255))
Layer(index=7, apply=<function sparkle at 0x0352D580>, name='sparkle', bg=(100, 170, 255))
Layer(index=8, apply=<function darken at 0x0352D5C8>, name='darken', bg=(30, 30, 30))
9
'''

