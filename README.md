# ChessPGNToPDF
Converts a PGN database to a pdf file with LaTeX.

Steps: 

(1) Install python, LaTeX, and the python module chess.py

(2) Edit the file "input.pgn" to include the games you want in the book. 

(3) Run the runner file using the command "Python3 runner.py" 

(4) Go into the tt directory. There should be a file called output.tex there.

(5) Now run the command "pdflatex output.tex". This will take a while, hit enter if the conversion stops of comes accross and errors. They will not effect the file it is just Latex saying something was wrong 
with the formatting of the PGN game its converting.

(6) There will not be a pdf file in the tt folder.
