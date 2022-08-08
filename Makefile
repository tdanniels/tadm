all:
	@mkdir -p bin
	@pandoc --pdf-engine=xelatex --variable monofont="Go Mono" \
		--filter pandoc-include-code src/solutions.md -s -o bin/solutions.pdf

.PHONY: test
test: checkpy testpy testrs

checkpy:
	@pyright python/src

testpy: export PYTHONPATH = python:python/src
testpy:
	@python -m unittest -b test

testrs:

clean:
	@rm -f bin/solutions.pdf
