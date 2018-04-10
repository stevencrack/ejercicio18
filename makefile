make dos: second1.png second2.png


second1.png second2.png: second.py data2.txt
	python second.py

data2.txt: second.exe
	./second.exe

second.exe: second.cpp
	c++ second.cpp -o second.exe



make uno: grafica1.png

grafica1.png: first.py data.txt
	python first.py

data.txt: first.exe
	./first.exe > data.txt

first.exe: first.cpp
	c++ first.cpp -o first.exe

