from setuptools import find_packages, setup
from setuptools_rust import Binding, RustExtension, Strip

VERSION = "1.1.0"

long_description = """
Python binding for nlpO3, a Thai natural language processing library in Rust.

## Features

- Thai word tokenizer
  - use maximal-matching dictionary-based tokenization algorithm and honor Thai Character Cluster boundaries
  - 2x faster than similar pure Python implementation (PyThaiNLP's newmm)
  - built-in dictionary included (62,000 words, a copy from PyThaiNLP)
  - support custom dictionary


## Install

```bash
pip install nlpo3
```

## Usage

Tokenization using default dictionary:
```python
from nlpo3 import segment

segment("สวัสดีครับ")
```

Load file `path/to/dict.file` to memory and assigned it with name `custom_dict`.
Then tokenize a text with `custom_dict` dictionary:
```python
from nlpo3 import load_dict, segment

load_dict("path/to/dict.file", "custom_dict")
segment("สวัสดีครับ", "custom_dict")

For more documentation, go [https://github.com/PyThaiNLP/nlpo3](https://github.com/PyThaiNLP/nlpo3)
"""

setup(
    name="nlpo3",
    version=VERSION,
    description="Python binding for nlpO3 Thai language processing library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    license="Apache-2.0",
    keywords=[
        "thai",
        "tokenizer",
        "nlp",
        "rust",
        "pythainlp",
    ],
    author=(
        "Thanathip Suntorntip, "
        "Arthit Suriyawongkul, "
        "Wannaphong Phatthiyaphaibun"
    ),
    author_email="wannaphong@yahoo.com",
    url="https://github.com/PyThaiNLP/nlpo3/",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: Thai",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    rust_extensions=[
        RustExtension(
            "nlpo3._nlpo3_python_backend",
            path="Cargo.toml",
            binding=Binding.PyO3,
            strip=Strip.No,
        )
    ],
    obsoletes=[
        "pythainlp-rust-modules",
    ],  # old package name
)
