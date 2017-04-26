#makefile

PY3 = python3
CMD = screenwriiter.py
PDF = pdflatex
DEL = rm -vf
ETE = out.tex out.log out.aux out.pdf ./txtsrc/out.tex


run:
	$(PY3) $(CMD) | $(PDF)

clean:
	$(DEL) $(ETE)
