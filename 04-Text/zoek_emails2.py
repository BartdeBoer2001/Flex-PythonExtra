import re
import io
import sys

emails = []

def email(txtnaam):
    with open("tekstmetemails.txt", "r") as bestand:
        regel = bestand.readline()
        while regel:
            patroon = r"\S+@\S+"
            gevonden = re.findall(patroon, regel)
            regel = bestand.readline()
            emails.extend(gevonden)
            bestand = open(txtnaam, "w")
            bestand.write(str(emails))

email(sys.argv[1])
