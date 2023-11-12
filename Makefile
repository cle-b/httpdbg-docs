.PHONY: setup docs clean

setup:
	python -m pip install pip --upgrade
	pip install -r requirements.txt

docs:
	mkdocs serve

clean:
	rm -rf .pytest_cache
	rm -rf __pycache__
	rm -rf httpdbg.egg-info
	rm -rf venv
	rm -rf build
	rm -rf dist
