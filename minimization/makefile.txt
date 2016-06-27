all: A

A: outputA.txt
	cat $<

outputA.txt: main.py minimization.py equations.py counter.py makefile.txt
	python $< > $@

clean:
	rm -rf __pycache__
	rm -r outputA.txt *.pyc
