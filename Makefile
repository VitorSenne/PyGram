install:
	poetry install

format:
	poetry remove prospector
	poetry add --group dev blue@latest
	blue .
	isort .
lint:
	poetry remove blue
	poetry add --group dev prospector@latest
	isort . --check
	prospector --with-tool pep257