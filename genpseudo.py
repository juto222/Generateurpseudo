import random

gaming = ["Shadow", "Vortex", "Ghost", "Sniper", "Hunter"]
hacker = ["Cyber", "Hack", "Root", "Admin", "Script"]
fantasy = ["Dragon", "Elf", "Wizard", "Knight", "Orc"]
futuristic = ["Neo", "Android", "Cyborg", "Matrix", "Nova"]

mots = gaming + hacker + fantasy + futuristic

config = {
    "numero": False,
    "caractere": False,
    "maj": False,
    "nbpseudo": 1,
}

numask = input("Ajouter des chiffres ? (y/n) : ")
if numask.lower() == "y":
    config["numero"] = True

carask = input("Ajouter des caractères spéciaux ? (y/n) : ")
if carask.lower() == "y":
    config["caractere"] = True

majask = input("Tout en majuscules ? (y/n) : ")
if majask.lower() == "y":
    config["maj"] = True

config["nbpseudo"] = int(input("Combien de pseudos ? : "))

def generate_pseudo():
    pseudos = []

    for _ in range(config["nbpseudo"]):
        pseudo = random.choice(mots)

        if config["numero"]:
            pseudo += str(random.randint(0, 999))

        if config["caractere"]:
            pseudo += random.choice(["_", ".", "-", "@"])

        if config["maj"]:
            pseudo = pseudo.upper()

        pseudos.append(pseudo)

    return pseudos

print("\nPseudos générés :")
for a in generate_pseudo():
    print("-", a)