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