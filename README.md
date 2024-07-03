# Quick Start

Ecosystem Plugin for berachain support in Ape.

## Dependencies

- [python3](https://www.python.org/downloads) version 3.9 up to 3.12.

## Installation

### via `ape`

You can install this plugin using `ape`:

```bash
ape plugins install berachain
```

or via config file:

```yaml
# ape-config.yaml
plugins:
  - name: berachain
```

### via `pip`

You can install the latest release via [`pip`](https://pypi.org/project/pip/):

```bash
pip install ape-berachain
```

### via `setuptools`

You can clone the repository and use [`setuptools`](https://github.com/pypa/setuptools) for the most up-to-date version:

```bash
git clone https://github.com/ApeWorX/ape-berachain.git
cd ape-berachain
python3 setup.py install
```

## Quick Usage

Installing this plugin adds support for the berachain ecosystem:

```bash
ape console --network berachain:bartio
```

## Development

Comments, questions, criticisms and pull requests are welcomed.