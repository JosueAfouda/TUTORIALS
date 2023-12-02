import time

def prepareCafe():
    print("Debut prepareCafe()")
    time.sleep(3) # On suppose que cette taâche prend 3 secondes
    print("Fin prepareCafe()")
    return "Le café est prêt"

def ToasterPain():
    print("Debut ToasterPain()")
    time.sleep(2) # On suppose que cette taâche prend 2 secondes
    print("Fin ToasterPain()")
    return "Le pain toasté est prêt"

def main():
    start_time = time.time()

    resultat_cafe = prepareCafe()
    resultat_toast = ToasterPain()

    end_time = time.time()
    duree = end_time - start_time

    print(f"Resulat de prepareCafe : {resultat_cafe}")
    print(f"Resultat de ToasterPain : {resultat_toast}")
    print(f"Temps total d'exécution : {duree:.2f} secondes")

if __name__ == "__main__":
    main()
