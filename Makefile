all:
	@mkdir -p bin
	@pandoc --pdf-engine=xelatex --variable monofont="Go Mono" \
		--filter pandoc-include-code src/solutions.md -s -o bin/solutions.pdf

.PHONY: test
test: checkpy testpy testrs

.PHONY: checkpy
checkpy:
	@pyright -p python python/src

.PHONY: testpy
testpy: export PYTHONPATH = python:python/src
testpy:
	@python -m unittest -b test

.PHONY: testrs
testrs:
	@for p in rust/**/Cargo.toml; do \
		cd "$$(dirname "$$p")" && cargo test && cd -; \
	done

.PHONY: clean
clean:
	@rm -f bin/solutions.pdf
