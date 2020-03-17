TEX		= pdflatex -shell-escape -interaction=nonstopmode -file-line-error
SHELL	= zsh
FILTERS	= -F pandoc-crossref -F pandoc-include-code -F pandoc-xnos
OPTIONS = --template=styles/template.tex
CONFIG  = --metadata-file config.yml
BIB     = --filter pandoc-citeproc --bibliography=references.bib
SRC     = $(shell ls $(SRC_DIR)/**/*.md)
SRC_DIR = sections
REPORT  = covid_19


pdf:
	pandoc $(CONFIG) $(OPTIONS) -s $(SRC) -o $(REPORT).pdf


clean:
	@echo "Cleaning..."
	@-cat .art/maid.ascii
	@rm $(REPORT).pdf
	@echo "...✓ done!"
