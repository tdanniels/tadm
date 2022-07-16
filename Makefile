all:
	@pandoc --pdf-engine=xelatex --variable monofont="Go Mono" \
		--filter pandoc-include-code solutions.md -s -o solutions.pdf

test:
	@pyright src/
	@python -m unittest test

clean:
	@rm -f solutions.pdf
