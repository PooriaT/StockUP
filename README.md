# StockUP
Stock Market AI assistant



pylint [options] packages/*/src
black {source_file_or_directory}
python -m black {source_file_or_directory}

poetry run black .
poetry run pre-commit run --all-files
poetry run pylint .



stockup/
├── app/
│   ├── __init__.py
│   ├── main.py                  # Main Streamlit entry point
│   ├── pages/
│   │   └── page1.py             # Additional Streamlit pages
│   ├── components/
│   │   └── header.py            # Reusable UI components
│   └── utils/
│       └── data_loader.py       # Utility functions
├── config/
│   ├── config.toml              # Global app settings
│   └── secrets.toml             # API keys, sensitive info
├── static/
│   ├── css/
│   │   └── styles.css           # CSS files
│   ├── img/
│   │   └── logo.png             # Image assets
│   └── js/
│       └── script.js            # Optional JS files
├── tests/
│   ├── unit/
│   │   └── test_components.py   # Unit tests
│   └── integration/
│       └── test_pages.py        # Integration tests
├── data/
│   └── sample_data.csv          # Data used by the app
├── .streamlit/
│   └── config.toml              # Streamlit server config
├── poetry.lock
├── pyproject.toml
└── README.md
