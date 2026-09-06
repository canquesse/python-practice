# Python Fundamentals

A focused collection of introductory Python notebooks, progressing from expressions and data types to reusable functions. Each notebook keeps one topic small enough to run and inspect in a single sitting.

[![Checks](https://github.com/canquesse/python-practice/actions/workflows/ci.yml/badge.svg)](https://github.com/canquesse/python-practice/actions/workflows/ci.yml)

## Suggested order

1. `variables and expressions/` — values, numeric and string types, basic expressions.
2. `conditionals/comparing.ipynb` — comparisons and branching.
3. `functions/defining_functions.ipynb` — defining and calling functions.
4. `functions/returning_values.ipynb` — return values and composition.
5. `functions/built_in_functions.ipynb` — built-in functions.
6. `functions/the_principles_of_code_reuse.ipynb` and `code_style.ipynb` — reuse and readability.

## Run

The examples use standard Python 3. To browse interactively:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install jupyterlab
jupyter lab
```

On Windows activate with `.venv\Scripts\activate`.

To execute all exercise cells from top to bottom without installing Jupyter:

```sh
python3 scripts/check_notebooks.py
```

The check isolates each notebook's namespace and fails on an execution error. Outputs are deliberately cleared in version control so the examples remain readable and produce fresh results when run.

## Scope

These are foundations exercises, not an application framework. For a complete data workflow with model comparison and evaluation, see [Iris Classification Lab](https://github.com/canquesse/iris-classification-lab).
