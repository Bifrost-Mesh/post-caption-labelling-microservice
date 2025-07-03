# Recommendation Engine

![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge)
![spaCy Badge](https://img.shields.io/badge/spaCy-09A3D5?logo=spacy&logoColor=fff&style=for-the-badge)
![PyTorch Badge](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=fff&style=for-the-badge)

## Development Environment setup

Prerequisites :

- [Nix](https://github.com/DeterminateSystems/nix-installer)
- [Direnv](https://direnv.net/)

Once you have them installed :

1. Allow `direnv` to automatically land you into the **Nix development shell environment**, whenever you cd into this directory :
    ```shell script
    direnv allow
    ```

2. Install Python package dependencies :
    ```shell script
    pip3 install --requirement requirements.txt
    ```

You can access `Marimo UI` at <http://localhost:8888>, by running :
```shell script
marimo edit \
  --headless \
  --host 192.168.29.146 --port 8888 \
  --no-token
```

## REFERENCEs

- [22: Recommendation Engine (YouTube, TikTok) | Systems Design Interview Questions With Ex-Google SWE](https://www.youtube.com/watch?v=QrZTmiZSRcw)

- [An overview of marimo](https://www.youtube.com/watch?v=3N6lInzq5MI)

- [Requirements File Format](https://pip.pypa.io/en/stable/reference/requirements-file-format/)

- [Writing your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)

- [Nix Flake for non-FHS venv](https://gist.github.com/agoose77/55d04420384cafac9b09971d4870b1f6)

- [Tokenization in NLP: Types, Challenges, Examples, Tools](https://neptune.ai/blog/tokenization-in-nlp)
