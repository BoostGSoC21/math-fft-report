VPATH=plots
docfiles:=gsoc-report.tex intro.tex state.tex api.tex app_ring.tex \
    quickstart.tex benchmarks.tex
target:=gsoc-report.pdf
main:=gsoc-report.tex
command:=rubber
options:=--pdf
plots:=complex_p2.pdf complex_p10.pdf complex_primes.pdf \
    real_p2.pdf real_p10.pdf real_primes.pdf

default: $(target)

$(target) : $(docfiles) $(plots)
	-$(command) $(options) $(main)

clean:
	-$(command) $(options) --clean $(main)

.PHONY: clean default
