all: A B

A: outputA.txt
	cat $<

outputA.txt: mainptA.py QRdecomp.py makefile.txt
	python $< > $@

B: outputB.txt
	cat $<

outputB.txt: mainptB.py givens.py makefile.txt
	python $< > $@

clean:
	rm -rf __pycache__
	rm -r outputA.txt outputB.txt
