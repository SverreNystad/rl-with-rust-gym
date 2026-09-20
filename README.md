# rl-with-rust-gym

uv run maturin develop

rl-with-rust-gym
├── src  # put python code in src folder
│   └── rl
│       ├── __init__.py
│       └── bar.py
├── pyproject.toml
├── README.md
├── rl.pyi # <<< add type stubs for Rust functions in the rl module here
└── rust_gym # put rust code in rust folder
    |── Cargo.toml
    └── src
        └── lib.rs
