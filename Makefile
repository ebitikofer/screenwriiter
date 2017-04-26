#makefile

PY3 = python3
CMD = screenwriiui.py
DEL = rm -vf
ETE = out.tex out.log out.aux out.pdf ./txtsrc/out.tex

run:
	$(PY3) $(CMD)

clean:
	$(DEL) $(ETE)
