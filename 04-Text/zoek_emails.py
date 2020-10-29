import re
import io

emails = []
with open("tekstmetemails.txt", "r") as bestand:
    regel = bestand.readline()
    while regel:
        patroon = r"\S+@\S+"
        gevonden = re.findall(patroon, regel)
        regel = bestand.readline()
        emails.extend(gevonden)
print(emails)

bestand = open("emails.txt", "w") #Dit is uitdaging 1
bestand.write(str(emails))
bestand.close()
