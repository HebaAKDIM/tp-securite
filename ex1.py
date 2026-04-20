import hashlib

# ════════════════════════════════════════════
#  1 & 2 — CHIFFREMENT / DÉCHIFFREMENT CÉSAR
# ════════════════════════════════════════════

def chiffrer(texte, cle):
    resultat = ""
    cle = ((cle % 26) + 26) % 26

    for c in texte:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            resultat += chr((ord(c) - base + cle) % 26 + base)
        else:
            resultat += c

    return resultat


def dechiffrer(texte, cle):
    return chiffrer(texte, -cle)


# ════════════════════════════════════════════
#  3 — CALCUL SHA-256
# ════════════════════════════════════════════

def sha256(texte):
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


# ════════════════════════════════════════════
#  4 — COMPARAISON DE HASHS
# ════════════════════════════════════════════

def comparer_hashs():
    print("\n  -- COMPARAISON DE HASHS SHA-256 --")
    print("  [A] Comparer deux TEXTES")
    print("  [B] Comparer deux HASHS")

    mode = input("\n  Votre choix (A/B) : ").strip().upper()

    if mode == "B":
        hash1 = input("\n  Hash 1 : ").strip().lower()
        hash2 = input("  Hash 2 : ").strip().lower()
    else:
        texte1 = input("\n  Texte 1 : ")
        texte2 = input("  Texte 2 : ")

        hash1 = sha256(texte1)
        hash2 = sha256(texte2)

        print("\n  SHA-256 texte 1 :", hash1)
        print("  SHA-256 texte 2 :", hash2)

    print("\n  +------------------------------------------+")

    if hash1 == hash2:
        print("  |  RESULTAT : [OK] HASHS IDENTIQUES         |")
        print("  |  => Aucune modification detectee          |")
    else:
        print("  |  RESULTAT : [!!] HASHS DIFFERENTS         |")
        print("  |  => MODIFICATION DETECTEE !               |")

    print("  +------------------------------------------+")

    # Détection des différences (optionnel)
    if mode != "B" and hash1 != hash2:
        print("\n  Premiers octets modifies :")
        diff = 0

        for i in range(0, min(len(hash1), len(hash2)) - 1, 2):
            b1 = hash1[i:i+2]
            b2 = hash2[i:i+2]

            if b1 != b2:
                print(f"    Octet {(i//2)+1:2} : {b1} --> {b2}")
                diff += 1

                if diff >= 5:
                    print("    ... (autres differences)")
                    break


# ════════════════════════════════════════════
#  MENU
# ════════════════════════════════════════════

def afficher_menu():
    print("\n  +------------------------------------------------+")
    print("  |      APPLICATION SECURITE & CHIFFREMENT        |")
    print("  +------------------------------------------------+")
    print("  |  1. Chiffrer un texte (Cesar)                  |")
    print("  |  2. Dechiffrer un texte (Cesar)                |")
    print("  |  3. Calculer le SHA-256                        |")
    print("  |  4. Comparer deux hashs                        |")
    print("  |  5. Quitter                                    |")
    print("  +------------------------------------------------+")


def lire_entier(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("  Veuillez saisir un entier valide.")


# ════════════════════════════════════════════
#  MAIN
# ════════════════════════════════════════════

def main():
    print("\n  Bienvenue dans l'application Securite & Chiffrement !")

    continuer = True

    while continuer:
        afficher_menu()
        choix = input("  Votre choix : ").strip()

        if choix == "1":
            print("\n  -- CHIFFREMENT CESAR --")
            texte = input("  Texte a chiffrer : ")
            cle = lire_entier("  Cle : ")

            print("\n  Texte original :", texte)
            print("  Texte chiffre  :", chiffrer(texte, cle))

        elif choix == "2":
            print("\n  -- DECHIFFREMENT CESAR --")
            texte = input("  Texte a dechiffrer : ")
            cle = lire_entier("  Cle : ")

            print("\n  Texte dechiffre :", dechiffrer(texte, cle))

        elif choix == "3":
            print("\n  -- SHA-256 --")
            texte = input("  Texte : ")
            hash_val = sha256(texte)

            print("\n  SHA-256 :", hash_val)
            print("  Longueur :", len(hash_val), "caracteres")

        elif choix == "4":
            comparer_hashs()

        elif choix == "5":
            print("\n  Au revoir !")
            continuer = False

        else:
            print("  Choix invalide !")


# Lancer le programme
if __name__ == "__main__":
    main()