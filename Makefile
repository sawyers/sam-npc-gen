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


prep-win:
	choco install python --version=3.8.0
	choco install wget
	choco install awscli
	python -m pip install pipenv --user
	pipenv install --dev
	pipenv run pre-commit install
	wget https://github.com/awslabs/aws-sam-cli/releases/latest/download/AWS_SAM_CLI_64_PY3.msi?raw=true -O AWS_SAM_CLI_64_PY3.msi
	msiexec /i "AWS_SAM_CLI_64_PY3.msi"
	del AWS_SAM_CLI_64_PY3.msi
	sam --version
	python --version


lint:
	pre-commit run --all-files


test-win:

update-dnd:
	# cd function dir
	# Start minimal docker that installs requirements
	# zip -r9 function.zip .
	# zip -g function.zip app.py
	# aws lambda update-function-code --function-name my-function --zip-file fileb://function.zip