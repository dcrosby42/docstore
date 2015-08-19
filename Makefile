VERSION=$(shell grep __version__ docstore/__init__.py)
REQUIREMENTS="requirements-dev.txt"
TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"

all: test

init: 
	@echo $(TAG)Installing dev requirements$(END)
	pip install --upgrade -r $(REQUIREMENTS)
	@echo

test: init
	@echo $(TAG)Running unit tests$(END)
	nosetests -sv
	@echo

clean:
	@echo $(TAG)Cleaning up$(END)
	find docstore -name '__pycache__' -delete -print -o -name '*.pyc' -delete -print
	find tests -name '__pycache__' -delete -print -o -name '*.pyc' -delete -print
	@echo
