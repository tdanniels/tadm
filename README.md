Solutions to odd-numbered problems from the second edition of The Algorithm Design Manual.

The text portions of the solutions under `src/` are written in Pandoc-flavoured
Markdown, and thus don't look very good in, e.g., Github's Markdown viewer.

To build a PDF of the solutions, run `make` in the project root.

To test the code portions of the solutions, run `make test` in the project root.

PDF dependencies:
- Pandoc
- XeLaTeX
- The [`pandoc-include-code`](https://hackage.haskell.org/package/pandoc-include-code)
filter.
- The [Go Mono](https://github.com/golang/image/blob/master/font/gofont/ttfs/Go-Mono.ttf)
font.

Test dependencies:
- Python (3.9+)
- A recent Rust compiler
- A C compiler
