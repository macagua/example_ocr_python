# DEVELOPMENT ENVIRONMENTS

Pre requirements dependencies

```console
sudo apt-get update
sudo apt-get install build-essential pkg-config python3-dev
virtualenv venv
source venv/bin/activate
pip install -U pip
pip install -r requirements/dev.txt
pre-commit install
```

## flake8

You can see all options for the script, executing the following command:

```console
python -m flake8 --help
```

Examples of the use:

```console
python -m flake8 images/extract_text.py
python -m flake8 pdfs/extract_text.py
```

## pycodestyle

You can see all options for the script, executing the following command:

```console
python -m pycodestyle --help
```

Examples of the use:

```console
python -m pycodestyle pdfs/extract_text.py
python -m pycodestyle images/extract_text.py
```

## pylint

You can see all options for the script, executing the following command:

```console
python -m pylint --help
```

Examples of the use:

```console
python -m pylint images/extract_text.py
python -m pylint pdfs/extract_text.py
```

## isort

You can see all options for the script, executing the following command:

```console
python -m isort --help
```

Examples of the use:

```console
python -m isort pdfs/extract_text.py
python -m isort images/extract_text.py
```

## black

You can see all options for the script, executing the following command:

```console
python -m black --help
```

Examples of the use:

Check the Python module without made changes it:

```console
python -m black images/extract_text.py --check
python -m black pdfs/extract_text.py --check
```

Fix the Python module:

```console
python -m black images/extract_text.py
python -m black pdfs/extract_text.py
```

## pydocstyle

You can see all options for the script, executing the following command:

```console
python -m pydocstyle --help
```

Examples of the use:

```console
python -m pydocstyle images/extract_text.py
python -m pydocstyle pdfs/extract_text.py
```

## mypy

You can see all options for the script, executing the following command:

```console
python -m mypy --help
```

Examples of the use:

```console
python -m mypy images/extract_text.py
python -m mypy pdfs/extract_text.py
```

## bandit

You can see all options for the script, executing the following command:

```console
python -m bandit --help
```

Examples of the use:

```console
python -m bandit -r images/extract_text.py
python -m bandit -r pdfs/extract_text.py
```

## wily

You can see all options for the script, executing the following command:

```console
python -m wily --help
```

## Build the wily cache.

```console
python -m wily build images/
python -m wily build pdfs/
```

### Show metrics for a given file.

Graph test.py against 'loc', 'sloc' and 'comments' (raw operator) metrics:

```console
python -m wily report images/extract_text.py loc sloc comments --message
python -m wily report pdfs/extract_text.py loc sloc comments --message
```

### Graph a specific metric for a given file

Graph a specific metric for a given file, if a path is given, all files
within path will be graphed.

Make a graph *.py files against 'loc' and 'sloc' (raw operator) metrics:

```console
python -m wily graph images/ loc sloc
python -m wily graph pdfs/ loc sloc
```

Make a graph *.py files against 'complexity' (cyclomatic operator) metrics:

```console
python -m wily graph images/ complexity
python -m wily graph pdfs/ complexity
```

## pre-commit

You can see all options for the script, executing the following command:

```console
pre-commit --help
```

Examples of the use:

```console
pre-commit run --all-files
```

## Ignore commit verification

```console
git commit --interactive --no-verify
```
