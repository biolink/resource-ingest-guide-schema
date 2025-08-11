MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:
.SUFFIXES:
.SECONDARY:

# environment variables
.EXPORT_ALL_VARIABLES:
ifdef LINKML_ENVIRONMENT_FILENAME
include ${LINKML_ENVIRONMENT_FILENAME}
else
include config.public.mk
endif

RUN = poetry run
SCHEMA_NAME = $(LINKML_SCHEMA_NAME)
SOURCE_SCHEMA_PATH = $(LINKML_SCHEMA_SOURCE_PATH)
SOURCE_SCHEMA_DIR = $(dir $(SOURCE_SCHEMA_PATH))
SRC = src
DEST = project
PYMODEL = $(SRC)/$(SCHEMA_NAME)/datamodel
DOCDIR = docs
DOCTEMPLATES = $(SRC)/docs/doc-templates

# Use += to append variables from the variables file
CONFIG_YAML =
ifdef LINKML_GENERATORS_CONFIG_YAML
CONFIG_YAML += "--config-file"
CONFIG_YAML += ${LINKML_GENERATORS_CONFIG_YAML}
endif

GEN_DOC_ARGS =
ifdef LINKML_GENERATORS_DOC_ARGS
GEN_DOC_ARGS += ${LINKML_GENERATORS_DOC_ARGS}
endif


# basename of a YAML file in model/
.PHONY: all clean setup gen-project gendoc

# note: "help" MUST be the first target in the file,
# when the user types "make" they should get help info
help: status
	@echo ""
	@echo "make install -- install dependencies"
	@echo "make test -- runs tests"
	@echo "make lint -- perform linting"
	@echo "make testdoc -- builds docs and runs local test server"
	@echo "make help -- show this help"
	@echo ""

# install any dependencies required for building
install:
	poetry install
.PHONY: install

all: site
site: gen-project gendoc
%.yaml: gen-project
deploy: all mkd-gh-deploy

# generates all project files
gen-project: $(PYMODEL)
	$(RUN) gen-project ${CONFIG_YAML} -d $(DEST) $(SOURCE_SCHEMA_PATH) && mv $(DEST)/*.py $(PYMODEL)


test: test-schema test-python

test-schema:
	$(RUN) gen-project ${CONFIG_YAML} -d tmp $(SOURCE_SCHEMA_PATH)

test-python:
	$(RUN) python -m pytest

lint:
	$(RUN) linkml-lint $(SOURCE_SCHEMA_PATH)

# Test documentation locally
serve: mkd-serve

# Python datamodel
$(PYMODEL):
	mkdir -p $@

$(DOCDIR):
	mkdir -p $@

gendoc: $(DOCDIR)
	cp $(SRC)/schema/resource_ingest_guide_schema/resource_ingest_guide_schema.yaml $(DOCDIR) ; \
	cp -r $(SRC)/docs/images $(DOCDIR)/images ; \
	$(RUN) gen-doc -d $(DOCDIR) --template-directory $(SRC)/docs/doc-templates/ $(SOURCE_SCHEMA_PATH)

testdoc: gendoc serve

MKDOCS = $(RUN) mkdocs
mkd-%:
	$(MKDOCS) $*

# only necessary if setting up via cookiecutter
.cruft.json:
	echo "creating a stub for .cruft.json. IMPORTANT: setup via cruft not cookiecutter recommended!" ; \
	touch $@

clean:
	rm -rf $(DEST)
	rm -rf tmp
	rm -fr $(DOCDIR)/*
	rm -fr $(PYMODEL)/*

include project.Makefile
