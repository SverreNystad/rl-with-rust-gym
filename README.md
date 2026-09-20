# rl-with-rust-gym

> **_NOTE:_** This project is inspired by two dear friends of mine: [Brage Kvamme](https://github.com/BrageHK) recently made a crazy cool project with a custom AlphaZero implementation in Rust then ported over to the browser with WebAssembly, and [Tim Matras](https://github.com/Artewald) that has been spreading the gospel of Rust for a long time. Inspired by them, I wanted to create a similar project that uses Rust for the environment and Python for the training loop.

The goal is to create a reinforcement learning environment in Rust and then use Python to train an agent in that environment.

## Prerequisites

- **Git**: Ensure that git is installed on your machine. [Download Git](https://git-scm.com/downloads)
- **Python 3.12**: Required for the project. [Download Python](https://www.python.org/downloads/)
- **UV**: Used for managing Python environments. [Install UV](https://docs.astral.sh/uv/getting-started/installation/)


## Usage
Run the training loop for a reinforcement learning agent in a Rust environment from Python.

```bash
uv run maturin develop
uv run trainer.py
```