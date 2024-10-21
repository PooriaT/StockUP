# StockUP
Stock Market AI assistant



pylint [options] packages/*/src
black {source_file_or_directory}
python -m black {source_file_or_directory}

poetry run black .
poetry run pre-commit run --all-files
poetry run pylint .



stockup/
├── app
│   ├── apis
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   └── stock_info.cpython-312.pyc
│   │   └── stock_info.py
│   ├── components
│   │   └── __init__.py
│   ├── __init__.py
│   ├── main.py
│   ├── pages
│   │   ├── about.py
│   │   ├── home.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── about.cpython-312.pyc
│   │       ├── app.cpython-312.pyc
│   │       ├── home.cpython-312.pyc
│   │       └── __init__.cpython-312.pyc
│   ├── __pycache__
│   │   └── __init__.cpython-312.pyc
│   └── utils
│       └── __init__.py
├── config
│   ├── config.toml
│   └── secrets.toml
├── Dockerfile
├── poetry.lock
├── pyproject.toml
├── pytest.ini
├── README.md
├── static
│   └── img
└── test
    ├── integration
    └── unit
        ├── apis
        │   ├── __pycache__
        │   │   └── test_stock_info.cpython-312-pytest-8.3.3.pyc
        │   └── test_stock_info.py
        └── pages
            └── __pycache__
                └── test_home.cpython-312-pytest-8.3.3.pyc




docker build -t stockup-app .
docker run -p 8501:8501 stockup-app
