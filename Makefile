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
	python3 -m pip install pipenv --user
	pipenv install --dev
	pipenv run pre-commit install
	curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
	unzip -o awscliv2.zip && sudo ./aws/install --update && rm awscliv2.zip
	rm -rf aws
	curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh | /bin/bash
	#test -d ~/.linuxbrew && eval $(~/.linuxbrew/bin/brew shellenv)
	#test -d /home/linuxbrew/.linuxbrew && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
	#test -r ~/.bash_profile && echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.bash_profile
	#echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile
	brew --version
	brew tap aws/tap
	brew install aws-sam-cli
	sam --version
	python3 --version


lint:
	pre-commit run


test-win:

update-dnd:
	# cd function dir
	# Start minimal docker that installs requirements
	# zip -r9 function.zip .
	# zip -g function.zip app.py
	# aws lambda update-function-code --function-name my-function --zip-file fileb://function.zip
