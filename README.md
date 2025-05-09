# vcd-tools
[![Tests Status](https://github.com/chiplukes/vcd-tools/actions/workflows/test.yml/badge.svg)]
[![Changelog](https://img.shields.io/github/v/release/chiplukes/vcd-tools?include_prereleases&label=changelog)](https://github.com/chiplukes/vcd-tools/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/chiplukes/vcd-tools/blob/main/LICENSE)

This is a simple project that can be used to start new python application.

## Installation

Install this application using `pip`:
```bash
git clone git+https://github.com/chiplukes/vcd-tools
cd vcd-tools
python -m venv .venv
source venv/bin/activate
# install this python application + dependencies
python -m pip install -e .

```

## Usage

### Help

```bash
python main.py -h
```

### Example finding a binary sequence from vcd file.
When run you are presented with a menu where you can mark () multiple signals from the vcd file
```bash
python main.py -a find_binary_pattern -p 0011111010,1100000101,0101111100,1010000011
python -m vcd_tools
```


### Example counting number of beats

Can select multiple signals that are AND'ed together and counted as a beat.  This is typically used for AXI Stream transactions.

```bash
python main.py -a count_beats
python -m vcd_tools
```

## Misc

For using pre-commit hooks:
```bash
pre-commit install
```
