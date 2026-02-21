# Python Joke Generator

A minimal Tkinter desktop app that displays a random programming joke when you click a button. The implementation is intentionally small (single file) to make it easy to run, review, and extend.

## At a glance

- **Type:** Desktop GUI
- **Language:** Python
- **UI:** Tkinter
- **Jokes:** `pyjokes`
- **Entry point:** `pythonjokegenerator.py`

## Features

- One-window GUI titled **“Python Joke Generator”**
- Starter prompt text
- **Generate Joke** button fetches a random joke via `pyjokes.get_joke()`

## Project layout

```
.
├── pythonjokegenerator.py
└── README.md
```

## Requirements

- Python 3 (any modern Python 3.x should work)
- Tkinter
  - Usually included with Python on Windows/macOS
  - Some Linux distros require installing it separately
- Python package: `pyjokes`

## Setup

### 1) Create a virtual environment (recommended)

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

Windows (cmd.exe):

```bat
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --upgrade pip
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### 2) Install dependencies

```bash
python -m pip install pyjokes
```

## Run

```bash
python pythonjokegenerator.py
```

## How it works (developer notes)

- The Tkinter window is created and configured (`title`, `geometry`).
- Clicking **Generate Joke** calls `generate_joke()`.
- `generate_joke()` calls `pyjokes.get_joke()` and updates the label with `joke_label.config(text=...)`.

This is a straightforward event-driven flow: Tkinter’s `mainloop()` waits for UI events and invokes the bound callback.

## Troubleshooting

- **`ModuleNotFoundError: No module named 'pyjokes'`**
  - Install it into the same environment you’re running: `python -m pip install pyjokes`.
  - If you’re using a venv, make sure it’s activated before installing/running.

- **Tkinter import fails on Linux**
  - Debian/Ubuntu: `sudo apt-get install python3-tk`

- **Multiple Python installs on Windows**
  - Prefer `python -m pip ...` to ensure pip targets the same interpreter.

## Extension ideas (optional)

- Wrap the UI into an `App` class to avoid module-level widget variables.
- Add a **Copy to clipboard** button.
- Add joke selection controls (category/language) if you choose to expose `pyjokes` options.
