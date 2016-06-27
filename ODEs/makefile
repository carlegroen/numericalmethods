all: A

A: output.txt
	cat $<

output.txt: main.py rungekutta.py makefile.txt
	python $< > $@

clean:
	rm -rf __pycache__
	rm -r output.txt
