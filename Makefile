.PHONY: help prepare-dev test lint run doc

.DEFAULT: help
help:
	@echo "make prepare-dev"
	@echo "		prepare develop environment, use only once"
	@echo "make test"
	@echo "		run tests"
	@echo "make lint"
	@echo " 	run black, bandit, and prettier"
	@echo "make run"
	@echo "		run project"

prepare-dev:
	sudo apt-get install python3
	python3 -m pip install pipenv --user
	pipenv install --dev
	pipenv run pre-commit install
	pipenv shell

lint:
	pre-commit run --all-files
