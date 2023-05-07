# DEVELOPMENT ENVIRONMENTS

Pre requirements dependencies

```console
sudo apt-get update
sudo apt-get install build-essential pkg-config python3-dev
virtualenv venv
source venv/bin/activate
pip install -U pip
pip install -r requirements/dev.txt
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

```console
python -m black images/extract_text.py --check
python -m black images/extract_text.py
python -m black pdfs/extract_text.py --check
python -m black pdfs/extract_text.py
```

## pydocstyle

You can see all options for the script, executing the following command:

```console
python -m pydocstyle --help
```

Examples of the use:

```console
python -m pydocstyle --help
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
