for file in subgame*.txt; do
	./open-spiel.py < $file > open-spiel-$file
done
