from __future__ import annotations
from data_structures.referential_array import ArrayR
from abc import ABC, abstractmethod
from layer_store import LayerStore, SetLayerStore, AdditiveLayerStore, SequenceLayerStore, T


class Grid(SetLayerStore[T], AdditiveLayerStore[T], SequenceLayerStore[T], ABC):
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

        LayerStore.__init__()
        self.draw_style = draw_style
        self.column = x
        self.row = y
        self.brush_size = self.DEFAULT_BRUSH_SIZE

        # 2D Grid
        self.First_dimension = ArrayR(self.column)  # e.g. y = 4, y = [None,None,None,None]
        # we want, y = [x,x,x,x]
        for i in range(len(self.First_dimension)):
            self.First_dimension.__setitem__(i, ArrayR(self.row))
        self.grid = self.First_dimension

        # create instance of one type of LayerStore for grid, according to draw style
        if self.draw_style == self.DRAW_STYLE_OPTIONS[0]:
            SetLayerStore.__init__()
        elif self.draw_style == self.DRAW_STYLE_OPTIONS[1]:
            AdditiveLayerStore.__init__()
        else:
            SequenceLayerStore.__init__()

    def __getitem__(self, x: int, y: int):
        return self.grid[x][y]

    def __setitem__(self, x: int, y: int, value: T):
        self.grid[x][y] = value

    def increase_brush_size(self):
        """
        Increases the size of the brush by 1,
        if the brush size is already MAX_BRUSH,
        then do nothing.
        """
        if self.brush_size == self.MAX_BRUSH:
            return
        else:
            self.brush_size += 1
            return

    def decrease_brush_size(self):
        """
        Decreases the size of the brush by 1,
        if the brush size is already MIN_BRUSH,
        then do nothing.
        """
        if self.brush_size == self.MIN_BRUSH:
            return
        else:
            self.brush_size -= 1
            return

    def special(self):
        """
        Activate the special affect on all grid squares.
        """
