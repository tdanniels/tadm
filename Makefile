all:
	@pandoc --pdf-engine=xelatex --variable monofont="Go Mono" \
		--filter pandoc-include-code solutions.md -s -o solutions.pdf

.PHONY: test
test:
	@pyright src/
	@python -m unittest -b test

clean:
	@rm -f solutions.pdf
