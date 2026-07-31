.PHONY: run test clean install

install:
	pip install -r requirements.txt

run:
	python main.py

test:
	pytest -v

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name "*.pyc" -delete
