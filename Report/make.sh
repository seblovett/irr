#!/bin/bash
#clean
rm IRR.aux
rm IRR.log
rm IRR.blg
rm IRR.bll
pdflatex -interaction=nonstopmode IRR.tex
if [ $? != 0 ]; then
	echo Error occurred...
	beep
	exit 1
fi
bibtex IRR
pdflatex -interaction=nonstopmode IRR.tex
pdflatex -interaction=nonstopmode IRR.tex
