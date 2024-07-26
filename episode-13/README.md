# Episode 13

Clock on the thumbnail below to watch the video:

[<img alt = "Episode 13a" src = "https://i.imgur.com/oWnEmPL.png" width = 25% />](https://youtu.be/FIvTuYDOeCc?list=PL6_bLxRDFzoKjaa3qCGkwR5L_ouSreaVP)

This episode is split into two parts:

- EP13a: The code has gotten a little crusty. This episode restructures the codebase, adds a `pyproject.toml` file and switches to Poetry for better dependency management, and adds a formatter and a linter as well as a CI setup to check all this.
- EP13b: Loading big save files took a long-ass time before this. This episode covers profiling and optimization techniques and rewrites a lot of the chunk loading code in Cython to speed it up dramatically. It also covers some frame time improvements in preparation for adding mobs.

## Installing dependencies

Using [Poetry](https://python-poetry.org/):

```console
poetry install
```

This will also build the Cython extensions.
If you ever need to rebuild them, you can do:

```console
poetry build
```

## Running

Again, using Poetry:

```console
poetry run python mcpy.py
```
