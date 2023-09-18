import os
import sys
from PyPDF2 import PdfReader, PdfWriter, errors


# Aktuální složka + /Locked_files
WORKING_DIR = os.getcwd()

# Funkce pro uzamknutí PDF souboru
def pdf_locker(pdf_file):
    pdf = PdfReader(pdf_file)
    pdf_lock = PdfWriter()

    for page in pdf.pages:
        pdf_lock.add_page(page)

    pdf_lock.encrypt(password)

    relative_path = os.path.relpath(pdf_file, WORKING_DIR)
    output_path = os.path.join(WORKING_DIR, "locked_files", relative_path)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "wb") as output:
        pdf_lock.write(output)

    print("||| ", relative_path, " |||")


def take_a_walk(path):
    locked = list()
    unread = list()
    counter = 0
    for root, _, files in os.walk(path):
        for soubor in files:
            if ("locked_files" in root): continue

            if soubor.lower().endswith(".pdf"):
                try:
                    cesta_ke_pdf = os.path.join(root, soubor)
                    pdf_locker(cesta_ke_pdf)
                    counter += 1
                    
                except errors.FileNotDecryptedError:
                    print()
                    print("CHYBA:")
                    print(f"Tento soubor '{soubor}' se zdá zaheslovaný, nechávám ho být.")
                    print()
                    locked.append(soubor)

                except errors.PdfReadError:
                    print()
                    print(f"CHYBA:")
                    print(f"Tento soubor '{soubor}' nelze otevřít z důvodu neznámé chyby, nechávám ho být.")
                    print()
                    unread.append(soubor)
        
                except Exception as e:
                    print(f"CHYBA U SOUBORU {soubor}")
                    print(e)
                    print(type(e))
                    sys.exit(f"Zastavuji, počet uzamčených souborů: {counter}")
    print(f"PDF soubory byly uzamčeny, celkový počet: '{counter}'")
    print()
    print("Souhrn již zamčených souborů: ", *locked if locked else "žádné")
    print()
    print("Souhrn neotevřitelných souborů: ", *unread if unread else "žádné")
    print()


if __name__ == "__main__":
    print("  #############################")
    print("#####                       #####")
    print("###      PDF LOCKER 3000       ###")
    print("#####                       #####")
    print("  #############################")

    print("Napište heslo, kterým chcete uzamknout všechna PDF")
    password = input("Po zadání stiskněte klávesu 'Enter': ")

    print("Uzamčené soubory: ")
    take_a_walk(WORKING_DIR)

    MADE_FOR = [
        "|   M   M  AAAAA  DDDD   EEEE     FFFF   OOO    RRRR    |",
        "|   MM MM  A   A  D   D  E        F     O   O   R   R   |",
        "|   M M M  AAAAA  D   D  EEE      FFF  O     O  RRRR    |",
        "|   M   M  A   A  D   D  E        F     O   O   R  R    |",
        "|   M   M  A   A  DDDD   EEEE     F      OOO    R    R  |"
    ]

    SARIVO = [
        "|        ####    ####   #####   #  #    #   ####        |",
        "|       #    #  #    #  #    #  #  #    #  #    #       |",
        "|       #       #    #  #    #  #  #    #  #    #       |",
        "|        ####   ######  #####   #  #    #  #    #       |",
        "|            #  #    #  #   #   #  #    #  #    #       |",
        "|       #    #  #    #  #   #   #   #  #   #    #       |",
        "|        ####   #    #  #    #  #    ##     ####        |"
    ]

    print(" " + "_"*55)
    print("|                                                       |")
    for row in MADE_FOR:
        print(row)
    print("|                                                       |")
    for row in SARIVO:
        print(row)

    print("|" + "_"*55 + "|")

    print()
    input("Pro ukončení stiskni 'Enter'")
