# Generator of graph families

This repository contains tools and resources for generating and exporting diverse families of graphs (Johnson, STS, ...) in several formats (DIMACS, LaTeX, etc).

## Usage

```python
./graphs.py name parameters [options]
```

## Families

### Johnson graphs

```python
./graphs.py johnson n k
```

Johnson graphs are a special class of undirected graphs defined from systems of sets. The vertices of the Johnson graph `J(n, k)` are the `k`-element subsets of an `n`-element set, where two vertices are adjacent when the intersection of the two vertices (subsets) contains `(k-1)`-elements.

![Johnson(4, 1)](https://raw.githubusercontent.com/jariazavalverde/graphs/master/images/johnson-4-1.png "Johnson(4, 1)") |![Johnson(4, 2)](https://raw.githubusercontent.com/jariazavalverde/graphs/master/images/johnson-4-2.png "Johnson(4, 2)")
:---: | :---:
[**Johnson(4, 1)**](https://github.com/jariazavalverde/graphs/blob/master/tex/johnson-4-1.tex) | [**Johnson(4, 2)**](https://github.com/jariazavalverde/graphs/blob/master/tex/johnson-4-2.tex)