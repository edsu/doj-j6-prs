all: inventory check

inventory:
	uv run inventory.py

check:
	uv run check.py
