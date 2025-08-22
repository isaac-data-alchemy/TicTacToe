.PHONY: build help

help:
	@echo ""
	@echo "Makefile Commands:"
	@echo "make build       - Build and recompile the application"
	@echo "make clean       - Clean up build artifacts"
	@echo ""

clean: 
	rm -rf build dist XANDO.spec
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	# Editor/IDE temporary files
	rm -rf .cache/ .pytest_cache/ .mypy_cache/ .coverage/ .vscode/
	# Node.js specific (if applicable)
	rm -rf node_modules/
	# General temporary files
	rm -f *.tmp *~ *.bak *.log

build:
	pyinstaller --onefile --collect-all tictactoe -n XANDO tictactoe/__main__.py