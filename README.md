# PDF Locker 3000
Jednoduchý script na uzamknutí všech PDF souborů uvnitř aktuálního adresáře a jeho podsložkách.

Nové PDF soubory jsou zkopírovány (a uzamčeny) do nové složky `./locked_files` přičemž jsou uchovány jejich relativní cesty.

## Dependencies
1. `PyPDF2` - _from PyPDF2 import PdfReader, PdfWriter_

Spouštěno na verzi Python 3.11.5

## Run
V konzoli spustíme script pomocí `python pdf-locker-3000.py`