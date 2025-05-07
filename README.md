# vcd-tools
[![Tests Status](https://github.com/chiplukes/vcd-tools/actions/workflows/test.yml/badge.svg)]
[![Changelog](https://img.shields.io/github/v/release/chiplukes/vcd-tools?include_prereleases&label=changelog)](https://github.com/chiplukes/vcd-tools/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/chiplukes/vcd-tools/blob/main/LICENSE)

This is a simple project that can be used to start new python application.

## Installation

Install this application using `pip`:
```bash
git clone git+https://github.com/chiplukes/vcd-tools
```

## Usage

## Development

To use this application, first checkout the code. Then create a new virtual environment:
```bash
cd vcd-tools
python -m venv .venv
source venv/bin/activate
```

Now install the dependencies and test dependencies:
```bash
python -m pip install -e .
```

Running main application
```bash
python -m vcd_tools
```

To run the tests:
```bash
pip install -e '.[test]'
pytest
```

For using pre-commit hooks:
```bash
pre-commit install
```
