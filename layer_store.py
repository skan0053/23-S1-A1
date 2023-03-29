from __future__ import annotations
from abc import ABC, abstractmethod

import layers
from layer_util import Layer, LAYERS, cur_layer_index
from typing import TypeVar, Generic
from data_structures.referential_array import ArrayR

T = TypeVar('T')


class LayerStore(ABC, Generic[T]):

    def __init__(self) -> None:
        self.length = 0

    @abstractmethod
    def add(self, layer: Layer) -> bool:
        """
        Add a layer to the store.
        Returns true if the LayerStore was actually changed.
        """
        pass

    @abstractmethod
    def get_color(self, start, timestamp, x, y) -> tuple[int, int, int]:
        """
        Returns the colour this square should show, given the current layers.
        """
        pass

    @abstractmethod
    def erase(self, layer: Layer) -> bool:
        """
        Complete the erase action with this layer
        Returns true if the LayerStore was actually changed.
        """
        pass

    @abstractmethod
    def special(self):
        """
        Special mode. Different for each store implementation.
        """
        pass


class SetLayerStore(LayerStore, ABC):
    """
    Set layer store. A single layer can be stored at a time (or nothing at all)
    - add: Set the single layer.
    - erase: Remove the single layer. Ignore what is currently selected.
    - special: Invert the colour output.
    """

    def __init__(self):
        LayerStore.__init__(self)
        self.SetLayer = ArrayR(1)  # Only single layer at time, therefore array size of 1

    def add(self, layer: Layer) -> bool:
        if layer not in self.SetLayer:
            self.SetLayer[0] = layer
            self.length += 1
            return True
        return False

    def get_color(self, start, timestamp, x, y) -> tuple[int, int, int]:
        # first u see what layer currently on top
        current_layer = self.SetLayer[0]
        for i in range(0, cur_layer_index - 1, 1):
            if current_layer is None:
                result = start
            elif current_layer.name == LAYERS[i].name:
                result = LAYERS[i].apply(start, timestamp, x, y)
        return result

    def is_empty(self) -> bool:
        return len(self.SetLayer) == 0

    def erase(self, layer: Layer) -> bool:
        if not self.is_empty():
            self.length -= 1
            return True
        return False

    def special(self):



class AdditiveLayerStore(LayerStore, ABC):
    """
    Additive layer store. Each added layer applies after all previous ones.
    - add: Add a new layer to be added last.
    - erase: Remove the first layer that was added. Ignore what is currently selected.
    - special: Reverse the order of current layers (first becomes last, etc.)
    """

    pass


class SequenceLayerStore(LayerStore, ABC):
    """
    Sequential layer store. Each layer type is either applied / not applied, and is applied in order of index.
    - add: Ensure this layer type is applied.
    - erase: Ensure this layer type is not applied.
    - special:
        Of all currently applied layers, remove the one with median `name`.
        In the event of two layers being the median names, pick the lexicographically smaller one.
    """

    pass
