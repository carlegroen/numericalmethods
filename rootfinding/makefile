all: A B

B: outputB.txt
	cat $<

outputB.txt: mainptB.py jacobiroots.py findroots.py counter.py makefile.txt
	python $< > $@

A: outputA.txt
	cat $<

outputA.txt: mainptA.py findroots.py equations.py counter.py makefile.txt
	python $< > $@

clean:
	rm -rf __pycache__
	rm -r outputA.txt outputB.txt
