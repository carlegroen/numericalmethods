# data: main
# 	python main.py > output.txt
# main: main.py
# clean:
# 	rm output.txt
all: A

A: outputA.txt
	cat $<

outputA.txt: mainptA.py QRdecomp.py makefile.txt
	python $< > $@

#B: outputB.txt
#	cat $<

#outputB.txt: mainB.py givens.py makefile.txt
#	python $< > $@

clean:
	rm -rf __pycache__
	rm -r outputA.txt #outputB.txt
