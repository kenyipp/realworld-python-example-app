test:
	RUN_MODE=testing pytest ./tests -s

sort-import:
	find . -name "*.py" -exec isort {} +

remove-unused-imports:
	find . -name "*.py" -exec autoflake --in-place --remove-all-unused-imports {} +

lint:
	flake8 .

lint-fix:
	autopep8 --in-place --aggressive --recursive .

coverage:
	python -m coverage run -m pytest
