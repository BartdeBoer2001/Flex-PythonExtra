#regular expression die nodig is: ^06-?\d[8]
import re

while True:
    invoer = input("Voer je telefoonnummer in: ")
    regular = "^06-?\d{8}$"
    matches = re.findall(regular, invoer)
    if (len(matches) > 0):
        break

print("Bedankt voor het invoeren van je nummer in het juiste formaat: ", matches[0])
