.PHONY: help prepare-dev test lint run doc

.DEFAULT: help
help:
	@echo "make prep-win"
	@echo "		prepare develop environment, use only once"
	@echo "make test"
	@echo "		run tests"
	@echo "make lint"
	@echo " 	run black, bandit, and prettier"
	@echo "make run"
	@echo "		run project"


init:
	pipenv install --dev
	pipenv run pre-commit install
	curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
		unzip awscliv2.zip && \
		sudo ./aws/install && \
		rm awscliv2.zip

	python --version

lint:
	pre-commit run
