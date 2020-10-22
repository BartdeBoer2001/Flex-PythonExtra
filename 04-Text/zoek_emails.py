import re

emails = []
with open("tekstmetemails.txt", "r") as bestand:
    regel = bestand.readline()
    while regel:
        patroon = r"\S+@\S+"
        gevonden = re.findall(patroon, regel)
        regel = bestand.readline()
        emails.extend(gevonden)
print(emails)
