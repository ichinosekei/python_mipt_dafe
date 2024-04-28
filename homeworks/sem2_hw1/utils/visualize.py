import os
from typing import Optional
from itertools import cycle
from enum import Enum
import warnings

import matplotlib.pyplot as plt
import numpy as np


FIGSIZE = (16, 9)


class Colors(Enum):
    PURPLE = "purple"
    CYAN = "cyan"
    BLUE = "blue"
    RED = "red"
    GREEN = "green"
    ORANGE = "orange"


def visualize_scatter(
    points: np.ndarray,
    labels: np.ndarray,
    colors: Optional[list[Colors]] = None,
    axis: Optional[plt.Axes] = None,
) -> None:
    if colors is None:
        colors = list(Colors)

    colors_cycle = cycle([color.value for color in colors])

    labels_unique = np.unique(labels)

    if axis is None:
        _, axis = plt.subplots(figsize=FIGSIZE)

    for label in labels_unique:
        label_mask = labels == label
        axis.scatter(*points[label_mask].T, color=next(colors_cycle))

    axis.grid(True)


def visualize_comparison(
    points: np.ndarray,
    prediction: np.ndarray,
    expectation: np.ndarray,
    colors: Optional[list[str]] = None,
    path_to_save: str = ''
) -> None:
    _, (ax1, ax2) = plt.subplots(1, 2, figsize=FIGSIZE)

    ax1.set_title("prediction", fontsize=15, fontweight="bold", c="dimgray")
    ax2.set_title("expectation", fontsize=15, fontweight="bold", c="dimgray")

    visualize_scatter(points, prediction, colors=colors, axis=ax1)
    visualize_scatter(points, expectation, colors=colors, axis=ax2)

    if len(path_to_save) != 0:
        if os.path.isfile(path_to_save):
            warnings.warn("В указанном пути есть файл, мы его заменили")
        plt.savefig(path_to_save)

    plt.show()
