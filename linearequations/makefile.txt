all: A B

A: outA.txt
	cat $<

outA.txt: mainptA.py QRdecomp.py makefile.txt
	python $< > $@

B: outB.txt
	cat $<

outB.txt: mainptB.py givens.py makefile.txt
	python $< > $@

clean:
	rm -rf __pycache__
	rm -r outA.txt outB.txt
