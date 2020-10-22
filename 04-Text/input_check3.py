#regular expression die nodig is: ^06-?\d[8]
#Voor het kenteken is [a-zA-Z]{2}-[0-9]{3}-[a-zA-Z]{3} nodig
import re

while True:
    invoer = input("Voer je telefoonnummer in: ")
    regular = "^06-?\d{8}$"
    matches = re.findall(regular, invoer)
    invoer2 = input("Voer nu jouw kenteken in: ")
    regular2 = "[a-zA-Z]{2}-[0-9]{3}-[a-zA-Z]{3}"
    matches2 = re.findall(regular2, invoer2)
    if (len(matches) > 0) and (len(matches2) > 0):
        break

print("Bedankt voor het invoeren van je nummer in het juiste formaat: ", matches[0])
print("En ook bedankt voor het kenteken: ", matches2[0])
