Tarvitset ainakin seuraavat python-moduulit (pip3 install --user moduulin_nimi):
python-Levenshtein
scikit-learn
numpy
Cython
pystemmer (vaati Cythonin jotta asentuu, https://github.com/snowballstem/pystemmer)

Jos tulee virheilmoituksia, tod näk virheestä näkyy että joku moduuli puuttuu.

Howto:
1. Laita kysymykset tiedostoon data/q.txt ja vastaukset (samoille rivinumeroille)
 tiedostoon data/a.txt

2. Aja tfidf_index.py

3. Aja tfidf.py

Voit suorittaa vaiheet 2-3 myös ajamalla skriptin train.sh

4. Aja search_tfidf.py (tämän avulla voit kysyä botilta kysymyksiä)
*SCORE kertoo varmuusasteen