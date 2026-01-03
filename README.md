# Python Joke Generator

A simple desktop app that generates random programming jokes.

This project uses **Tkinter** for the GUI and the **pyjokes** library to fetch a random joke when you click a button.

## What it does

- Opens a small window titled **"Python Joke Generator"**
- Shows some starter text
- When you click **Generate Joke**, it fetches a random joke and updates the text on screen

## How it works (high level)

The app is a single Python file: `pythonjokegenerator.py`.

- Tkinter creates the main window (`root`), a label (`joke_label`), and a button (`generate_button`).
- The button is wired to the `generate_joke()` function via `command=generate_joke`.
- When clicked, `generate_joke()` calls `pyjokes.get_joke()` and updates the label text using `joke_label.config(text=joke)`.
- `root.mainloop()` starts the Tkinter event loop so the window stays responsive.

## Requirements

- Python 3.x
- `pyjokes`
- Tkinter (usually included with Python on Windows/macOS; may require an extra package on some Linux distros)

## Installation

### 1) (Optional) Create and activate a virtual environment

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies

```bash
pip install pyjokes
```

## Run the app

From the project folder:

```bash
python pythonjokegenerator.py
```

A window will open. Click **Generate Joke** to display a random joke.

## Troubleshooting

- **ModuleNotFoundError: No module named 'pyjokes'**
  - Run: `pip install pyjokes` (make sure you’re installing into the same Python environment you run).

- **Tkinter not found (Linux)**
  - On Debian/Ubuntu, you may need: `sudo apt-get install python3-tk`

## Project structure

```
2026-PythonJokeGenerator/
  pythonjokegenerator.py
  README.md
```
