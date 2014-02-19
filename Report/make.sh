#!/bin/bash
#clean
rm IRR.aux
rm IRR.log
rm IRR.blg
rm IRR.bll
pdflatex IRR.tex
if [ $? != 0 ]; then
	echo Error occurred...
	exit 1
fi
bibtex IRR
pdflatex IRR.tex
pdflatex IRR.tex
