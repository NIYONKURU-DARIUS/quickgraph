"""
graphs.py
Simple graphing helper functions for quickgraph.
"""
import matplotlib.pyplot as plt


def _finish(title, xlabel, ylabel, save, show):
    """Adds labels, then saves and/or shows the graph."""
    plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    plt.tight_layout()
    if save:
        plt.savefig(save)
    if show:
        plt.show()
    plt.close()


def line_graph(x: list, y: list, title: str = "Line Graph",
               xlabel: str = "", ylabel: str = "",
               save: str = None, show: bool = True) -> None:
    """Draws a line graph of y against x."""
    if len(x) != len(y):
        raise ValueError("x and y must have the same length.")
    plt.plot(x, y, marker="o")
    _finish(title, xlabel, ylabel, save, show)


def bar_graph(labels: list, values: list, title: str = "Bar Graph",
              xlabel: str = "", ylabel: str = "",
              save: str = None, show: bool = True) -> None:
    """Draws a bar graph with one bar per label."""
    if len(labels) != len(values):
        raise ValueError("labels and values must have the same length.")
    plt.bar(labels, values)
    _finish(title, xlabel, ylabel, save, show)


def pie_graph(labels: list, values: list, title: str = "Pie Graph",
              save: str = None, show: bool = True) -> None:
    """Draws a pie graph showing each value as a percentage."""
    if len(labels) != len(values):
        raise ValueError("labels and values must have the same length.")
    plt.pie(values, labels=labels, autopct="%1.1f%%")
    _finish(title, "", "", save, show)


def scatter_graph(x: list, y: list, title: str = "Scatter Graph",
                  xlabel: str = "", ylabel: str = "",
                  save: str = None, show: bool = True) -> None:
    """Draws a scatter graph of points (x, y)."""
    if len(x) != len(y):
        raise ValueError("x and y must have the same length.")
    plt.scatter(x, y)
    _finish(title, xlabel, ylabel, save, show)


def draw(kind: str, **inputs) -> None:
    """Draws any graph by name: 'line', 'bar', 'pie' or 'scatter'."""
    kinds = {
        "line": line_graph,
        "bar": bar_graph,
        "pie": pie_graph,
        "scatter": scatter_graph,
    }
    if kind not in kinds:
        raise ValueError(f"Unknown graph type '{kind}'. Choose from: {list(kinds)}")
    kinds[kind](**inputs)