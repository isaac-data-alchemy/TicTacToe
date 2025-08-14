# XANDO – Tic Tac Toe Game 🎮

XANDO is a terminal-based Tic Tac Toe (X and O) game implemented in Python using **Object-Oriented Programming**.  
It supports player vs player and player vs AI, with an interactive board display.

---

## 📂 Project Structure

tictactoe/
│── board.py # Board rendering and display logic
│── game.py # Game play rules and turn logic
│── player.py # Player and AIPlayer classes
│── sessions.py # Session management (rematch, quit, restart)
│── symbols.py # Symbol and color handling
│── main.py # Main entry point
│── init.py
tests/
│── unit/ # Unit tests for board and player
pyproject.toml # Project metadata
Makefile # Build automation script (⚠ see note below)


---

## 🚀 Running the Game (From Source)

From the root directory, run:

```bash
python -m tictactoe

🛠 Building the Application (Executable)

This project includes a Makefile to build a standalone executable using PyInstaller.

⚠ Important – Makefile Placement

The Makefile must be placed outside the tictactoe/ package directory in order to build correctly.
If the Makefile sits inside tictactoe/, PyInstaller will fail due to package import issues.

✅ Correct structure for building:

project-root/
│── Makefile
│── tictactoe/
│── tests/
│── pyproject.toml


❌ Incorrect structure (will cause error):

tictactoe/
│── Makefile   # 🚫 Do not place here
│── board.py
│── ...

📦 Build Commands

To build:

make build


To clean previous builds:

make clean

🔹 Makefile Commands
.PHONY: build help

help:
	@echo ""
	@echo "Makefile Commands:"
	@echo "make build       - Build and recompile the application"
	@echo "make clean       - Clean up build artifacts"
	@echo ""

clean: 
	rm -rf build dist XANDO.spec

build:
	pyinstaller --onefile --collect-all tictactoe -n XANDO tictactoe/__main__.py


📋 Requirements

Python 3.8+

colorama

pyinstaller (for building executable)

Install dependencies:

pip install -r requirements.txt

🎯 Running the Built Executable

After building, run:

./dist/XANDO


(Or dist\XANDO.exe on Windows)

🧪 Running Unit Tests

From the root directory:

pytest

📜 License

MIT License. Free to use and modify.


---
