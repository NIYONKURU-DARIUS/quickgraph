# 📊 QuickGraph (`quickgraph-darius12`)

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Package](https://img.shields.io/badge/TestPyPI-quickgraph--darius12-orange.svg)](https://test.pypi.org/project/quickgraph-darius12/)

> **Draw beautiful graphs in one line of code.**

`quickgraph` is a lightweight Python data visualization wrapper built on top of [Matplotlib](https://matplotlib.org/). It simplifies common plotting workflows (line plots, bar charts, pie charts, scatter plots) into clean, one-line function calls without boilerplates.

---

## 🚀 Key Features

- **⚡ Effortless One-Liners**: Generate plots with simple lists or arrays.
- **🎨 Multiple Graph Types**:
  - 📈 **Line Graph**: Track trends and sequential data with automatic markers.
  - 📊 **Bar Graph**: Compare categorical data across categories.
  - 🥧 **Pie Graph**: Visualize distributions and percentages with automatic percent labels.
  - 🔵 **Scatter Graph**: Spot correlations and relationships between two continuous variables.
- **🔀 Unified `draw()` Dispatcher**: Render any graph type through a single dynamic entrypoint: `draw("bar", ...)`.
- **💾 Save or Display**: Easily toggle whether to save figures to disk, display them interactively with `plt.show()`, or both.

---

## 📦 Installation

### From TestPyPI (Recommended)
```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple quickgraph-darius12
```

### Local Development Installation
Clone the repository and install in editable mode:
```bash
git clone https://github.com/NIYONKURU-DARIUS/quickgraph.git
cd quickgraph
pip install -e .
```

---

## 🛠️ Usage & Examples

### 1. Line Graph
```python
from quickgraph import line_graph

# Simple line chart
line_graph(
    x=[1, 2, 3, 4, 5],
    y=[2, 4, 9, 16, 25],
    title="Growth Trend",
    xlabel="Time (Weeks)",
    ylabel="Score",
    show=True
)
```

### 2. Bar Graph
```python
from quickgraph import bar_graph

# Categorical comparison
bar_graph(
    labels=["Computer Science", "Engineering", "Business", "Arts"],
    values=[85, 78, 92, 64],
    title="Average Performance by Department",
    xlabel="Department",
    ylabel="Average Grade (%)",
    save="performance.png",
    show=True
)
```

### 3. Pie Graph
```python
from quickgraph import pie_graph

# Percentage distribution
pie_graph(
    labels=["Python", "JavaScript", "C++", "Java"],
    values=[45, 25, 15, 15],
    title="Programming Language Usage",
    show=True
)
```

### 4. Scatter Graph
```python
from quickgraph import scatter_graph

# Correlation plot
scatter_graph(
    x=[2, 4, 5, 8, 10, 12],
    y=[50, 62, 68, 80, 89, 95],
    title="Study Hours vs. Exam Score",
    xlabel="Study Hours / Week",
    ylabel="Final Exam Score",
    show=True
)
```

### 5. Unified `draw()` Dispatcher
```python
from quickgraph import draw

# Easily switch graph types dynamically
draw("line", x=[1, 2, 3], y=[10, 20, 15], title="Dynamic Line")
draw("bar", labels=["X", "Y", "Z"], values=[30, 50, 20], title="Dynamic Bar")
draw("pie", labels=["Pass", "Fail"], values=[85, 15], title="Pass Rate")
draw("scatter", x=[1, 2, 3], y=[3, 2, 1], title="Dynamic Scatter")
```

---

## 📂 Project Structure

```text
quickgraph/
├── pyproject.toml              # Build system & package metadata
├── LICENSE                     # MIT License
├── README.md                   # Documentation & examples
└── src/
    └── quickgraph/
        ├── __init__.py         # Package exports (draw, line_graph, etc.)
        └── graphs.py           # Core plotting functions and dispatcher
```

---

## ⚙️ Building the Package

To build source distribution and wheel packages:
```bash
pip install --upgrade build twine
python -m build
```

---

## 👤 Author

- **Darius NIYONKURU**
- Email: [dariusniyonkuru351@gmail.com](mailto:dariusniyonkuru351@gmail.com)
- GitHub: [@NIYONKURU-DARIUS](https://github.com/NIYONKURU-DARIUS)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.