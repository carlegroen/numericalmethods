all: A

A: output.txt
	cat $<

output.txt: main.py integration.py counter.py makefile.txt
	python $< > $@

clean:
	rm -rf __pycache__
	rm -r output.txt
