# Generator of graphs

This repository contains tools and resources for generating, drawing and exporting diverse families of graphs (Johnson graphs, generalized Petersen graphs, ...) in several formats (DIMACS, LaTeX, etc).

## Usage

```python
./graphs.py name parameters [options]
```

## Families

* [Complete graphs](#complete-graphs)
* [Generalized Petersen graphs](#generalized-petersen-graphs)
* [Johnson graphs](#johnson-graphs)

### Complete graphs

A complete graph is an undirected graph in which every pair of distinct vertices is connected by a unique edge.

```python
./graphs.py complete n
```
where:
* `n` > `0`

![K(10)](https://raw.githubusercontent.com/jariazavalverde/graphs/master/images/complete-10.png "K(10)") | ![K(11)](https://raw.githubusercontent.com/jariazavalverde/graphs/master/images/complete-11.png "K(11)") | ![K(12)](https://raw.githubusercontent.com/jariazavalverde/graphs/master/images/complete-12.png "K(12)")
:---: | :---: | :---:
[**K(10)**](https://github.com/jariazavalverde/graphs/blob/master/tex/complete.tex) | [**K(11)**](https://github.com/jariazavalverde/graphs/blob/master/tex/complete.tex) | [**K(12)**](https://github.com/jariazavalverde/graphs/blob/master/tex/complete.tex)

The file [complete.tex](https://github.com/jariazavalverde/graphs/blob/master/tex/complete.tex) defines a LaTeX command `\complete{n}` for drawing any complete graph with TikZ.

### Generalized Petersen graphs

The generalized Petersen graphs are a family of cubic graphs formed by connecting the vertices of a regular polygon to the corresponding vertices of a star polygon. They include the Petersen graph and generalize one of the ways of constructing the Petersen graph.

```python
./graphs.py petersen n k
```
where:
* `n` > `0`
* `k` > `0`
* `k` < `n/2`

![GP(5, 1)](https://raw.githubusercontent.com/jariazavalverde/graphs/master/images/petersen-5-1.png "GP(5, 1)") | ![GP(5, 2)](https://raw.githubusercontent.com/jariazavalverde/graphs/master/images/petersen-5-2.png "GP(5, 2)") | ![GP(7, 1)](https://raw.githubusercontent.com/jariazavalverde/graphs/master/images/petersen-7-1.png "GP(7, 1)")
:---: | :---: | :---:
[**GP(5, 1)**](https://github.com/jariazavalverde/graphs/blob/master/tex/petersen.tex) | [**GP(5, 2)**](https://github.com/jariazavalverde/graphs/blob/master/tex/petersen.tex) | [**GP(7, 1)**](https://github.com/jariazavalverde/graphs/blob/master/tex/petersen.tex)

The file [petersen.tex](https://github.com/jariazavalverde/graphs/blob/master/tex/petersen.tex) defines a LaTeX command `\petersen{n}{k}` for drawing any generalized Petersen graph with TikZ.

### Johnson graphs

Johnson graphs are a special class of undirected graphs defined from systems of sets. The vertices of the Johnson graph `J(n, k)` are the `k`-element subsets of an `n`-element set, where two vertices are adjacent when the intersection of the two vertices (subsets) contains `(k-1)`-elements.

```python
./graphs.py johnson n k
```
where:
* `n` > `0`
* `k` > `0`
* `k` < `n`

![J(4, 1)](https://raw.githubusercontent.com/jariazavalverde/graphs/master/images/johnson-4-1.png "J(4, 1)") |![J(4, 2)](https://raw.githubusercontent.com/jariazavalverde/graphs/master/images/johnson-4-2.png "J(4, 2)")
:---: | :---:
[**J(4, 1)**](https://github.com/jariazavalverde/graphs/blob/master/tex/johnson-4-1.tex) | [**J(4, 2)**](https://github.com/jariazavalverde/graphs/blob/master/tex/johnson-4-2.tex)