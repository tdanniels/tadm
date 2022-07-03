all:
	pandoc solutions.md -s -o solutions.pdf

clean:
	rm -f solutions.pdf
