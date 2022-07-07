all:
	@pandoc --pdf-engine=xelatex --variable monofont="JetBrains Mono" \
		--filter pandoc-include-code solutions.md -s -o solutions.pdf

test:
	@pyright src/
	@for f in src/*.py; do python "$$f"; done

clean:
	@rm -f solutions.pdf
