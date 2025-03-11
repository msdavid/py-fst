# py-fst Development Guidelines

## Project Information
- License: Apache 2.0
- Author: msdavid (mauro@sauco.net)
- GitHub: https://github.com/msdavid/py-fst

## Build and Test Commands
- Install for development: `pip install -e .`
- Run all tests: `python -m unittest discover tests`
- Run a single test: `python -m unittest tests.test_fst.TestFST.test_write_read_fst`
- Run test script: `python test_script.py`

## Code Style Guidelines
- **Imports**: Standard library first, then third-party, then local modules; alphabetical within groups
- **Formatting**: 4-space indentation, 88-char line length (Black compatible)
- **Docstrings**: NumPy style (Parameters/Returns sections with types)
- **Type hints**: Use them for function signatures and return types
- **Naming**: snake_case for functions/variables, CamelCase for classes; avoid single-letter names
- **Error handling**: Use specific exceptions, document potential exceptions in docstrings
- **R integration**: Handle R's 1-based indexing carefully, reset DataFrame indexes after conversion

## Key Dependencies
- pandas: For DataFrame manipulation
- rpy2: For R integration
- R with 'fst' package: Required for functionality