# pythonplusplus

## Step 1: Create venv and install dependencies

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -R requirements.txt
```

## Step 2: Create the Executable

Use PyInstaller to create the executable:

1. **Navigate to project directory**: Navigate to the directory containing `main.py` script.
2. **Run PyInstaller**: Execute the following command to bundle script:

```sh
pyinstaller --distpath . --name python --onefile main.py
```

## Step 3: Run the Executable

After PyInstaller finishes, you’ll find the standalone executable in the root directory of the project. You can run it like any other binary executable.

On **Unix-based systems (Linux/macOS)**:

```sh
./python --debug script.py
```

On **Windows**:

```sh
python.exe --debug script.py
```
